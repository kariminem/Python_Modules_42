# Module 09 — Cosmic Data (Pydantic Models & Validation)

This module teaches **Pydantic 2.x**, a library that checks data against a schema you
describe with a class. If the data doesn't fit, Pydantic raises a `ValidationError`
that lists every problem it found. Each exercise adds one idea:

| Exercise | File | New concept |
|---|---|---|
| ex0 | `ex0/space_station.py` | `BaseModel` + `Field(...)` constraints, type coercion |
| ex1 | `ex1/alien_contact.py` | `Enum` fields + `@model_validator(mode="after")` business rules |
| ex2 | `ex2/space_crew.py` | Nested models (`List[CrewMember]`) + rules that look across the whole crew |

Subject constraints to remember: Python 3.10+, `flake8` clean, full type hints checked
with `mypy`, Pydantic v2 installed with `pip` inside a virtual environment, and **no
deprecated `@validator`**. Use `@model_validator` instead.

---

## Setup & running

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "pydantic>=2" flake8 mypy

python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py

flake8 ex0 ex1 ex2
mypy ex0/space_station.py ex1/alien_contact.py ex2/space_crew.py
```

All three scripts print exactly the subject's expected output. `flake8` and `mypy`
both pass with no issues.

---

## Key Pydantic concepts used everywhere

### `BaseModel`
You inherit from `BaseModel` and declare fields as **type-annotated class attributes**.
Pydantic reads these annotations and generates the `__init__` and the validation for you.

```python
class SpaceStation(BaseModel):
    crew_size: int = Field(ge=1, le=20)
```

### `Field(...)`
`Field` adds constraints and defaults to one field:

| Argument | Meaning | Applies to |
|---|---|---|
| `min_length` / `max_length` | length limits | `str`, `list` |
| `ge` / `le` | **g**reater-or-**e**qual / **l**ess-or-**e**qual | numbers |
| `default=` | value used when the field is omitted | any |

A field **without** a default (e.g. `last_maintenance: datetime`) is **required**.
A field with a plain default (e.g. `is_operational: bool = True`) is optional.

### `ValidationError`
Pydantic runs **every** check and collects all failures before raising one
`ValidationError`. `error.errors()` returns a list of dicts. Each dict has:
- `"loc"`: where the error is, e.g. `('crew_size',)` or `('crew', 0, 'age')`
- `"msg"`: the human-readable message, e.g. `"Input should be less than or equal to 20"`
- `"type"`: machine code, e.g. `"less_than_equal"`
- `"input"`: the bad value

The programs print only `detail["msg"]` so the output matches the subject.

### Type coercion (lax mode)
By default Pydantic **converts** compatible input rather than rejecting it:
- `"2024-01-15T10:30:00"` → `datetime(2024, 1, 15, 10, 30)`
- `"6"` → `6` for an `int` field
- `"radio"` → `ContactType.RADIO` for an enum field
- a `dict` → a `CrewMember` instance for a nested model field

Pydantic rejects input it can't convert, such as `"abc"` for an `int` field.

---

## Exercise 0 — Space Station Data (`ex0/space_station.py`)

**Goal:** basic model creation with `BaseModel` and `Field` validation.

### The model

```python
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)
```

Each line maps directly to one requirement in the subject:
- String lengths → `min_length` / `max_length`
- Numeric ranges → `ge` / `le`
- `last_maintenance: datetime` has no default, so it is **required**
- `is_operational: bool = True` → defaults to `True` when not given
- `notes: Optional[str] = Field(default=None, max_length=200)` can be missing
  (`None`). If it's given, it must be at most 200 chars. `max_length` only applies
  to actual strings, so `None` passes.

### `display_station(station)`
Prints the fields. `status` is computed with a conditional expression:
`"Operational" if station.is_operational else "Offline"`.

### `main()`
1. **Valid case.** It uses `SpaceStation.model_validate({...})`, which is the v2 way to
   validate raw data such as parsed JSON. The dict gives `last_maintenance` as the
   **string** `"2024-01-15T10:30:00"`, and Pydantic turns it into a `datetime`. This
   shows the coercion the subject asks about in "Think About".
2. **Invalid case.** It builds a station with `crew_size=25`. This breaks `le=20`, so
   Pydantic raises `ValidationError`. The `except` block loops over `error.errors()`
   and prints each `msg` → `Input should be less than or equal to 20`.

Both cases are wrapped in `try/except ValidationError`, which is the "exception
handling protects the data stream" requirement: bad data never crashes the program.

### "Think About" answers
- **How does automatic type conversion work?** In the default *lax* mode, Pydantic
  tries to coerce input to the annotated type. Strings of digits become ints, ISO
  strings become datetimes, and so on. Strict mode (`Field(strict=True)` or
  `ConfigDict(strict=True)`) turns this off.
- **String timestamp to a datetime field?** It is parsed as ISO 8601 and stored as
  a real `datetime` object. `station.last_maintenance` is a `datetime`, not a `str`.

---

## Exercise 1 — Alien Contact Logs (`ex1/alien_contact.py`)

**Goal:** custom validation with `@model_validator` for rules that involve **several
fields at once**. `Field` constraints can't express those.

### `ContactType` enum

```python
class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
```

Inheriting from **both `str` and `Enum`** makes each member also a string. That means:
- Pydantic accepts the raw string `"radio"` and converts it to `ContactType.RADIO`.
- Any other value (e.g. `"smoke"`) is rejected with an "Input should be 'radio',
  'visual', ..." error.
- `.value` gives the plain string (`"radio"`), which is used when printing.

### The model
The fields follow the same `Field(...)` pattern as ex0. The new part is
`contact_type: ContactType`, a field that must be one of the enum values.

### The model validator

```python
@model_validator(mode="after")
def check_business_rules(self) -> "AlienContact":
    if not self.contact_id.startswith("AC"):
        raise ValueError('Contact ID must start with "AC"')
    if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
        raise ValueError("Physical contact reports must be verified")
    if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
        raise ValueError("Telepathic contact requires at least 3 witnesses")
    if self.signal_strength > 7.0 and not self.message_received:
        raise ValueError("Strong signals (> 7.0) should include received messages")
    return self
```

Important points:
- **`mode="after"`** means this runs **after** all field-level checks pass. Here
  `self` is a fully built instance with correct types, so `self.witness_count` is
  guaranteed to be an `int` between 1 and 100. If a field check fails, this
  validator never runs.
- **Raise `ValueError`**, not `ValidationError`. Pydantic catches the `ValueError`
  and wraps it into a `ValidationError`, adding the prefix `"Value error, "` to the
  message.
- **`return self` is mandatory.** An after-validator must return the model. If it
  doesn't, the constructor gets `None` back.
- The return annotation `"AlienContact"` is a string (forward reference) because the
  class isn't fully defined yet when the method is written. This keeps mypy happy.
- The rules are checked in order, and the first failing one raises.
- `not self.message_received` catches both `None` and the empty string `""`.

### `show_error(error)`
Prints each `msg` with `.removeprefix("Value error, ")`, so the output is exactly
`Telepathic contact requires at least 3 witnesses` as the subject shows.

### `main()`
1. **Valid:** a radio contact with signal 8.5 **and** a message. It passes all rules,
   including the "strong signal needs a message" rule.
2. **Invalid:** a telepathic contact with `witness_count=1`. Every field constraint
   passes (1 is within 1–100), but the business rule fails. This shows exactly why
   `@model_validator` is needed.

---

## Exercise 2 — Space Crew Management (`ex2/space_crew.py`)

**Goal:** nested models, meaning a model that contains a list of other models, and
validation rules that look across the whole list.

### `Rank` enum
Same `str, Enum` pattern as ex1: `cadet`, `officer`, `lieutenant`, `captain`,
`commander`.

### `CrewMember` model
A plain model with `Field` constraints (age 18–80, experience 0–50, etc.) and
`is_active: bool = True`. It has no custom validator. It is the building block.

### `SpaceMission` model
The key line is:

```python
crew: List[CrewMember] = Field(min_length=1, max_length=12)
```

- `List[CrewMember]` tells Pydantic that **each item** must be validated as a
  `CrewMember`. You can pass `CrewMember` objects or plain dicts; dicts are turned
  into `CrewMember` automatically.
- On a list, `min_length` / `max_length` limit the **number of items** (1–12 members).
- `mission_status: str = "planned"` is a simple default.

### The mission validator

```python
@model_validator(mode="after")
def check_safety_requirements(self) -> "SpaceMission":
    if not self.mission_id.startswith("M"): ...

    leaders = [m for m in self.crew if m.rank in (Rank.COMMANDER, Rank.CAPTAIN)]
    if not leaders: ...

    if self.duration_days > 365:
        experienced = [m for m in self.crew if m.years_experience >= 5]
        if len(experienced) * 2 < len(self.crew): ...

    inactive = [m.name for m in self.crew if not m.is_active]
    if inactive: ...
    return self
```

- **Leader rule:** a list comprehension collects crew whose rank is commander or
  captain. An empty list means the rule fails.
- **Long-mission rule:** "at least 50% experienced" is written as
  `len(experienced) * 2 < len(crew)`. This uses integer math only, so there is no
  float division and no rounding issue. With 3 crew, 2 experienced passes
  (4 ≥ 3) and 1 experienced fails (2 < 3).
- **Active rule:** it collects the *names* of inactive members so the error message
  can say who is inactive.
- Because this is `mode="after"`, every `CrewMember` in `self.crew` is already
  validated when the method runs, so `m.rank` and `m.years_experience` are safe to use.

### `display_mission(mission)`
Prints the mission, then loops over `mission.crew` and prints
`- name (rank.value) - specialization` for each member.

### `main()`
1. It builds a `crew` list of three `CrewMember`s: a commander, a lieutenant, and an
   officer.
2. **Valid:** Mars mission, 900 days. It is a long mission, so it needs ≥50%
   experienced: Sarah (20 years) and John (10 years) are 2 of 3, so it passes. It has
   a commander, so it passes.
3. **Invalid:** Moon mission using `crew[1:]`, which is the same list **without Sarah**.
   Now nobody is a commander or captain → `Mission must have at least one Commander
   or Captain`.

### "Think About" answers
- **How does Pydantic validate nested models?** Recursively. It validates the outer
  fields, and for `crew` it validates each element as a `CrewMember`, running all
  of `CrewMember`'s constraints. After that, `SpaceMission`'s after-validator runs.
- **What happens if a `CrewMember` fails inside a `SpaceMission`?** The whole
  `SpaceMission` fails with a `ValidationError`, and the error's `loc` shows the
  exact path to the bad value. For example, a crew member aged 12 gives:

  ```
  1 validation error for SpaceMission
  crew.0.age
    Input should be greater than or equal to 18
  ```

  `crew.0.age` means field `crew`, item index `0`, field `age`. The mission-level
  `@model_validator` does **not** run, because field validation already failed.

---

## Possible evaluation questions

- **Why `@model_validator` and not `@field_validator` for these rules?** Every rule
  here involves two or more fields, such as contact type + witnesses, or duration +
  crew experience. A field validator only sees one field.
- **Why not `@validator`?** It is Pydantic v1 syntax, deprecated in v2, and the
  subject forbids it.
- **`mode="after"` vs `mode="before"`?** `before` receives the raw input (usually a
  dict) before any parsing. `after` receives the finished, typed instance. `after`
  is simpler and type-safe for business rules.
- **Why raise `ValueError` inside the validator?** Pydantic converts it into a
  `ValidationError` entry, so callers only need to catch one exception type.
- **Why `str, Enum`?** It lets raw strings from JSON/CSV map straight to enum members,
  and `.value` gives the display string.
- **`model_validate(dict)` vs `Model(**kwargs)`?** They validate the same way.
  `model_validate` is meant for data you already have as a dict, such as parsed JSON.

---

## About the provided `data_generator` tar

The subject ships `data_generator.py` and `data_exporter.py` as **helper tools** to
generate test data (JSON/CSV/Python). They are *not* exercise deliverables. The
subject's submission section says:

> You need to return only the files requested by the subject of this activity.

The requested files are only `ex0/space_station.py`, `ex1/alien_contact.py`, and
`ex2/space_crew.py`. **Do not push the tar or the tools** to the submission repo.
