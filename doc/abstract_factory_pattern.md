# Abstract factory pattern

* [It's a creational design pattern that lets you produce families of related objects without specifying their concrete classes.](https://refactoring.guru/design-patterns/abstract-factory)


## Problem 

- Imagine that you are building a GUI for windows and macOS.

- The component used are **Button**, **CheckBox**.

- If the user wants to use component from the same family i.e (Windows, MacOS), they must be consistent along the program, so if he chooses windows, the user must be provided with all the windows components (related objects) like **Button** and **CheckBox** .

So: 

- **Without using Abstract factory** :
```python
class WindowsButton:
    def render(self):
        print("Windows Button")


class MacButton:
    def render(self):
        print("Mac Button")


class WindowsCheckBox:
    def render(self):
        print("Windows CheckBox")


class MacCheckBox:
    def render(self):
        print("Mac CheckBox")


os_name = "windows"

if os_name == "windows":
    button = WindowsButton()
    checkbox = WindowsCheckBox()
else:
    button = MacButton()
    checkbox = MacCheckBox()

button.render()
checkbox.render()
```

* This is fine for small projects, but every time you add a new widget (TextBox, Menu, etc.) or a new OS (Linux), you'll need to modify many places.

The Abstract Factory guarantees that related objects are created together.

- With Abstract factory:

**Product interface:**
```python
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass
```

**Concrete products**
```python
class WindowsButton(Button):
    def render(self):
        print("Windows Button")


class MacButton(Button):
    def render(self):
        print("Mac Button")


class WindowsCheckBox(CheckBox):
    def render(self):
        print("Windows CheckBox")


class MacCheckBox(CheckBox):
    def render(self):
        print("Mac CheckBox")
```

**Abstract Factory**
```python
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass
```

**Concrete Factories**
```python
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckBox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckBox()
```


**Client code**
```python 
def build_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()


factory = WindowsFactory()
build_ui(factory)
```


## Benefits
1) Consistency: all created objects belong to the same family.
Loose coupling: client code depends on interfaces, not concrete classes.

2) Easy extensibility: adding Linux support means creating:

  - LinuxButton
  - LinuxCheckBox
  - LinuxFactory

without changing existing client code.

3) Centralized creation logic: object creation is in one place instead of scattered everywhere.

---

### Why not just create objects directly?

We absolutely can if:

- There are only a few classes.
- You don't expect new platforms.
- Consistency between families isn't important.

The Abstract Factory becomes useful when:

- You have multiple related products (Button, CheckBox, Menu, TextField, etc.).
They must be used together.
New product families (Windows, macOS, Linux) may be added later.

> In short, the pattern isn't about making object creation possible—it already is. It's about ensuring compatible objects are created together while keeping the client independent of the specific platform.
