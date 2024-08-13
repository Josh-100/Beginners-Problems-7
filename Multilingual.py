num_people = int(input("How many people are there? "))
all_languages = []
common_languages = None

for i in range(1, num_people + 1):
    num_languages = int(input(f"(To person {i}) How many languages can you speak? "))
    languages = set()
    for _ in range(num_languages):
        language = input(f"What languages can you speak in? ")
        languages.add(language)
    
    all_languages.append(languages)
    
    if common_languages is None:
        common_languages = languages
    else:
        common_languages &= languages

total_languages_spoken = set().union(*all_languages)

print(f"\nNumber of languages everyone speaks: {len(common_languages)}")
print(f"Spoken language(s) everyone speaks: {', '.join(sorted(common_languages))}")
print(f"Total languages spoken in the group: {len(total_languages_spoken)}")
print(f"Languages spoken: {', '.join(sorted(total_languages_spoken))}")