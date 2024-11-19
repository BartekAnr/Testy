school = {"Class A":
            {"English":
                ["John", "Helen", "Peter", "Joseph"],
             "Polish":
                ["Helen", "Bert", "Jospeh", "Jim"],
             "History":
                ["Jim", "Bert", "John", "Peter"],
             "Music":
                ["Helen", "Jopseh"]
            },
          "Class B":
            {"English":
                ["Jimi", "Golden", "Hizzy", "Woo"],
             "Polish":
                ["Woo", "Belik", "Hizzy", "Conny"],
             "History":
                ["Eren", "Fill", "Woo", "Golden"],
             "Music":
                ["Jimi", "Heni"]
            },
          "Class C":
            {"English":
                ["Moly", "Bitsy", "Paol", "Celin"],
             "Polish":
                ["Peny", "Kitty", "Bitsy", "Felix"],
             "History":
                ["Moly", "Paol", "Felix", "Kitty"],
             "Music":
                ["Moly", "Sily"]
            }
         }

print(school)

school["Class D"] = {"English":
                        ["Hsii", "Pauli", "Nik", "Collman"],
                     "Polish":
                        ["Collman", "Solt", "Pauli", "Patta"],
                     "History":
                        ["Kix", "Hsii", "Leoaa", "Solt"],
                     "Music":
                        ["Hsii", "Kix"]}

print(school)
print("")

for class_name, lessons in school.items():
    for subject, students in lessons.items():
        if "Paol" in students:
            students.remove("Paol")

print(school)
print("")

music_students = []

for class_name, lessons in school.items():
    if "Music" in lessons:
        music_students.extend(lessons["Music"])

print("Uczniowie zapisani na muzyke we wszystkich klasach:", set(music_students))
