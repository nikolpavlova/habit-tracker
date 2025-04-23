# 📘 Java Version – Habit Tracker CLI

This folder contains the Java implementation of the Habit Tracker application.

## 📁 Structure

- `model/` – Contains `Habit.java`
- `service/` – Contains `HabitManager.java`
- `cli/` – Contains the entry point `Main.java`

## ▶️ How to Compile and Run

```bash
cd src/java/cli
javac -d ../../compiled ../model/Habit.java ../service/HabitManager.java Main.java
cd ../../compiled
java cli.Main
```

## 🧪 Running Tests (planned)

JUnit tests can be added in the `tests/java/` folder.

## 💡 Notes

- This version mirrors the Python logic, showcasing Java's OOP structure and static typing.
