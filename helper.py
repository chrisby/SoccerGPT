import json
from functools import cache
from string import Formatter
import requests

sportmonks_token = "YOUR_KEY"
base_url = "https://api.sportmonks.com/v3/football"

position_dict = {
    24: "Goalkeeper",
    25: "Defender",
    26: "Midfielder",
    27: "Attacker",
    28: "Unknown",
    148: "Center Back",
    149: "Defensive Midfielder",
    150: "Attacking Midfielder",
    151: "Center Forward",
    152: "Left Wing",
    153: "Central Midfielder",
    154: "Right Back",
    155: "Left Back",
    156: "Right Wing",
    157: "Left Midfield",
    158: "Right Midfield",
    163: "Secondary Striker",
    221: "Coach",
    226: "Assistant Coach",
    227: "Goalkeeping Coach",
    228: "Forward Coach",
    560: "Caretaker Manager",
}

team_stats = {
    51: "On average, the team caused {average} offsides per game.",
    84: "On average, the team received {average} yellow cards per game.",
    56: "On average, the team performed {average} fouls per game.",
    47: "The team scored {scored} penalties, and missed {missed}.",
    216: "The team lost {count} game(s). This is {percentage}% of all games played.",
    88: "The team conceded {count} goals in total and {average} goals per game.",
    78: "The team performed {count} tackles and {average} tackles per game.",
    52: "The team scored {count} goals, with {average} goals per game.",
    215: "{count} of the team's game(s) resulted in a draw. This is {percentage}% of all games played.",
    45: "The team's ball possession was {average}%",
    214: "The team won {count} game(s). This is {percentage}% of all games played.",
    194: "In {percentage}% of all games, their opponent did not score a single goal (clean sheet).",
    34: "On average, the team took {average} corners per game.",
    44: "On average, the team performed {average} dangerous attacks per game.",
    211: "The highest rated player ({player_name}) had a rating of {rating}",
    9681: "{conversion_rate_pct}% of all shots were successfully converted into a goal.",
    9676: "On average, the team collected {average_points_per_game} points per game.",
    1677: "Out of all {total} shots, {on_target} were on target, {off_target} were off target, {inside_box} were shot inside of the box, {outside_box} outside the box, and {blocked} were blocked.",
    9682: "{pct_shots_on_target}% of all shots were on the target.",
    9675: "{right} players are right footed, {left} players are left footed.",
    47: "The conversion rate of penalties is {conversion_rate}%.",
    43: "On average, the team performed {average} attacks per game.",
    213: "{0-15}% of all conceded goals were conceded in the first 15 minutes, {15-30}% between minute 15 and 30, {30-45}% between minute 30 and 45, and {45-60}% were conceded in the last 15 minutes.",
    196: "{0-15}% of all scored goals were scored in the first 15 minutes, {15-30}% between minute 15 and 30, {30-45}% between minute 30 and 45, and {45-60}% were scored in the last 15 minutes.",
    191: "In {over_0_5}% of the games, the team scored at least 1 goal, in {over_1_5}% of the games they scored at least 2 goals, in {over_2_5}% of the games they scored at least 3 goals, in {over_3_5}% of the games they scored at least 4 goals, in {over_4_5}% of the games they scored at least 5 goals, in {over_5_5}% of the games they scored at least 6 goals.",
    59: "Average number of substitutions per game: {average}.",
    188: "The team played a total of {count} matches.",
    79: "Number of assists: {total}",
    119: "Minutes played: {value}",
    321: "Number of appearances: {total}",
    323: "Started from the bench {total} times.",
    100: "Performed {total} interceptions.",
    106: "Won {total} duels.",
    105: "Number of all duels: {total}.",
    107: "Won {total} aerials.",
    1584: "Passed {total}% passes accurately.",
    118: "Average rating: {average}.",
    40: "Played as captain {total} times.",
    86: "Number of shots on the target: {total}.",
    41: "Number of shots off the target: {total}.",
    42: "Total number of shots: {total}.",
    94: "Was dispossessed {total} times.",
    97: "Blocked {total} shots.",
    123: "Won {total} long balls.",
    98: "Number of total crosses: {total}.",
    99: "Number of accurate crosses: {total}.",
    580: "Created {total} big chances.",
    9676: "On average, the team earned {average_points_per_game} points per game.",
}
player_stats = {
    59: "The player was substituted in {in} times, and substituted out {out} times.",
    215: "{count} of the games were draws.",
    216: "The team lost {count} game(s).",
    188: "The team played a total of {count} matches.",
    52: "Number of goals: {total}, {penalties} through penalties.",
    79: "Number of assists: {total}",
    88: "Number of goals conceded: {total}",
    119: "Total minutes played: {total}",
    321: "Number of appearances: {total}",
    323: "Started from the bench {total} times.",
    47: "Won {won} penalties, scored {scored} penalties, committed {committed} penalties, and missed {missed} penalties.",
    56: "Performed {total} fouls.",
    78: "Performed {total} tackles.",
    100: "Performed {total} interceptions.",
    84: "Received {total} yellow cards.",
    106: "Won {total} duels.",
    105: "Number of all duels: {total}.",
    107: "Won {total} aerials.",
    1584: "Passed {total}% passes accurately.",
    118: "Average rating: {average}.",
    40: "Played as captain {total} times.",
    86: "Number of shots on the target: {total}.",
    41: "Number of shots off the target: {total}.",
    42: "Total number of shots: {total}.",
    94: "Was dispossessed {total} times.",
    97: "Blocked {total} shots.",
    123: "Won {total} long balls.",
    98: "Number of total crosses: {total}.",
    99: "Number of accurate crosses: {total}.",
    51: "Was offside {total} times.",
    580: "Created {total} big chances.",
    9676: "On average, the team earned {average_points_per_game} points per game.",
}

PLAYER_STATS_PROMPT_TEMPLATE = """\
For the {season} {league}, where he played as {position} for {team}, we have the following statistics:"""


def get_team_stats(statistic, relevant_stats, quali_stats_prompt):

    detail_type_ids = [detail["type_id"] for detail in statistic["details"]]
    detail_prompts = {
        id: relevant_stats[id] for id in detail_type_ids if id in relevant_stats
    }

    for detail_id, detail_prompt in detail_prompts.items():
        # Get the right detail
        detail = [
            detail for detail in statistic["details"] if detail["type_id"] == detail_id
        ][0]

        if detail_id in [213, 196]:
            keywords = [
                i[1] for i in Formatter().parse(detail_prompt) if i[1] is not None
            ]
            kwargs = {k: detail["value"][k]["percentage"] for k in keywords}
            stat_prompt = detail_prompt.format(**kwargs)

        elif detail_id in [191]:
            keywords = [
                i[1] for i in Formatter().parse(detail_prompt) if i[1] is not None
            ]
            kwargs = {k: detail["value"][k]["team"]["percentage"] for k in keywords}
            stat_prompt = detail_prompt.format(**kwargs)
        elif detail_id not in [216, 88, 52, 214, 194, 215]:
            keywords = [
                i[1] for i in Formatter().parse(detail_prompt) if i[1] is not None
            ]
            kwargs = {k: detail["value"][k] for k in keywords}
            stat_prompt = detail_prompt.format(**kwargs)
        else:
            keywords = [
                i[1] for i in Formatter().parse(detail_prompt) if i[1] is not None
            ]
            kwargs = {k: detail["value"]["all"][k] for k in keywords}
            stat_prompt = detail_prompt.format(**kwargs)

        quali_stats_prompt += f"\n - {stat_prompt}"

    return quali_stats_prompt


def get_player_stats(statistic, relevant_stats, quali_stats_prompt):
    detail_type_ids = [detail["type_id"] for detail in statistic["details"]]
    detail_prompts = {
        id: relevant_stats[id] for id in detail_type_ids if id in relevant_stats
    }

    for detail_id, detail_prompt in detail_prompts.items():
        # Get the right detail
        detail = [
            detail for detail in statistic["details"] if detail["type_id"] == detail_id
        ][0]
        keywords = [i[1] for i in Formatter().parse(detail_prompt) if i[1] is not None]

        kwargs = {k: detail["value"][k] for k in keywords}
        stat_prompt = detail_prompt.format(**kwargs)

        quali_stats_prompt += f"\n - {stat_prompt}"

    return quali_stats_prompt


@cache
def get_type_by_id(id):
    # Todo load json
    file_name = "./types.json"
    file_path = Path(file_name)
    types = {}
    if file_path.is_file():
        with open(file_name, "r") as f:
            types = json.load(f)

    if types:
        if id in types:
            return types[id]
        else:
            print(f"Call API because id {id} not in  types")
            url = f"https://api.sportmonks.com/v3/core/types/{id}?api_token={sportmonks_token}"
            r = requests.get(url)

            if r.status_code == 200:
                type_entry = json.loads(r.content)["data"]
                types[id] = type_entry
                with open(file_name, "w") as f:
                    # Write to file
                    json.dump(types, f, indent=4)
                return type_entry
            else:
                raise ValueError(f"Id {id} not found")
    else:
        print("Call API because tpyes doesn't exist")
        url = f"https://api.sportmonks.com/v3/core/types/{id}?api_token={sportmonks_token}"
        r = requests.get(url)

        if r.status_code == 200:
            type_entry = json.loads(r.content)["data"]
            types[id] = type_entry
            with open(file_name, "w") as f:
                # Write to file
                json.dump(types, f, indent=4)
            return type_entry
        else:
            raise ValueError(f"Id {id} not found")


@cache
def get_by_id(element_name, element_id, include=None, filters=None):
    url = f"{base_url}/{element_name}/{element_id}?api_token={sportmonks_token}"
    if include:
        url += f"&include={include}"
    if filters:
        url += f"&filters={filters}"

    r = requests.get(url)
    if r.status_code == 200:
        if "data" in json.loads(r.content):
            return json.loads(r.content)["data"]
        else:
            return None


def get_user_prompt(
    fixture,
    include_player_stats=True,
    prefix_prompt=None,
    suffix_prompt=None,
    by_team=False,
):
    if by_team:
        result = {}

    full_prompt = prefix_prompt

    for team in fixture["participants"]:
        team = get_by_id("teams", team["id"], include="players;statistics.details")

        # Get coach details
        coach_prompt = None
        coaches_details = get_by_id(
            "coaches",
            f"countries/{team['country_id']}",
            include="statistics.details;teams",
        )

        # API retrieves the wrong coach for Germany...
        for coach_details in coaches_details:
            for statistic in coach_details["statistics"]:
                season = get_by_id("seasons", statistic["season_id"])
                league = get_by_id("leagues", season["league_id"])

                if season["name"] == "2024" and league["name"] == "Euro Qualification":
                    coach_prompt = f"{coach_details['firstname']} {coach_details['lastname']}, born {coach_details['date_of_birth']}"
                    break

        full_prompt += f"\n\nHere are some statistics about the team \"{team['name']}\""

        if coach_prompt:
            full_prompt += f", which will be coached by {coach_prompt}.\n"
        else:
            full_prompt += ".\n"

        for statistic in team["statistics"]:  # Also stats for Germany are empty...
            # Only consider the european qualifications and the tournament
            season = get_by_id("seasons", statistic["season_id"])
            if season:  # We do not have access to all seasons
                league = get_by_id("leagues", season["league_id"])

                if league["name"] == "Euro Qualification" and season["name"] == "2024":
                    # This year's qualification

                    # Stats info
                    quali_stats = "During the qualifications for the 2024 European Championship, {team} achieved the following statistics:"
                    quali_stats_prompt = quali_stats.format(team=team["name"])

                    stats_prompt = get_team_stats(
                        statistic, team_stats, quali_stats_prompt
                    )
                    full_prompt += stats_prompt

                elif (
                    league["name"] == "European Championship"
                    and season["name"] == "2024"
                ):
                    # TODO: this year's tournament
                    pass
                else:
                    continue

        # Player statistics
        if include_player_stats:
            full_prompt += f"\n\nHere are the statistics of some players of the team \"{team['name']}\":"
            all_stats = ""
            for player in team["players"]:
                player_details = get_by_id(
                    "players", player["player_id"], include="statistics.details"
                )

                # Get position
                if player_details["detailed_position_id"]:
                    pos = position_dict[player_details["detailed_position_id"]]
                else:
                    pos = position_dict[player_details["position_id"]]

                for statistic in player_details["statistics"]:
                    season = get_by_id("seasons", statistic["season_id"])
                    league = get_by_id("leagues", season["league_id"])

                    if (
                        league["name"] == "Euro Qualification"
                        and season["name"] == "2024"
                    ):
                        team = get_by_id("teams", statistic["team_id"])
                        position = position_dict[statistic["position_id"]]

                        stats_str = PLAYER_STATS_PROMPT_TEMPLATE.format(
                            season=season["name"],
                            league=league["name"],
                            team=team["name"],
                            position=position,
                        )

                        if statistic["details"]:
                            stats_prompt = get_player_stats(statistic, player_stats, "")
                            all_stats += f'\n\nName: {player_details["firstname"]} {player_details["lastname"]}, born {player_details["date_of_birth"]}, position: {pos}:\n'
                            all_stats += stats_str
                            all_stats += stats_prompt
            if all_stats:
                full_prompt += all_stats
        if by_team:
            result[team["name"]] = full_prompt
            # Reset full prompt
            full_prompt = ""

    if by_team:
        return result
    else:
        full_prompt += suffix_prompt
        return full_prompt
