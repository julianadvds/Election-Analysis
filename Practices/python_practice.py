# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])

# #if"El paso" in counties:
#     print("El Paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or el Paso is not in the list of counties")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#     print("Arapahoe and el Paso is not in the list of counties")

#for i in range(len(counties)):
 #   print(counties[i])

# counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

# for county in counties_dict.keys():
#     print(county)

# for county in counties_dict.values():
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])
#     print (county)

# for county in counties_dict:
#     print(counties_dict.get(county))

# for key, value in counties_dict.items():
#         print(key +" county has " + str(value) + " registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


# for county_dict in voting_data:
#         print(county_dict)

# for county_dict in range(len(voting_data)):
#     print(voting_data[county_dict])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)