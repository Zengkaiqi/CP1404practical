"""
wimbledon
Estimate: 20 minutes
Actual:   27 minutes
"""
FILENAME = "wimbledon.csv"
def main():
    countries,winners = open_wimbledon_csv()
    winner_count = count_win_times(winners)
    unique_country = remove_repeat_country(countries)
    for winner in winner_count:
        print(f"{winner} win {winner_count[winner]} times")
    print(f"These {len(unique_country)} countries have won Wimbledon:")
    print(",".join(unique_country))

def count_win_times(winners):
    del winners[0]
    winners.sort()
    winner_to_count = {}
    for winner in winners:
        if winner in winner_to_count:
            winner_to_count[winner] += 1
        else:
            winner_to_count[winner] = 1
    return winner_to_count
def open_wimbledon_csv():
    countries = []
    winners = []
    with (open(FILENAME, "r", encoding="utf-8-sig") as in_file):
        for line in in_file:
            parts = line.split(",")
            countries.append(parts[1])
            winners.append(parts[2])
    return countries, winners

def remove_repeat_country(countries):
    del countries[0]
    unique_countries = list(set(countries))
    unique_countries.sort()
    return unique_countries

main()