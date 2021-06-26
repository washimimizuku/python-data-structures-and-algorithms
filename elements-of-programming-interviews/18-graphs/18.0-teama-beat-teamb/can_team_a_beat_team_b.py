import collections

'''
Given teams A and B, is there a sequence of teams starting
with A and ending with B such that each team in the sequence
has beaten the next team in the sequence?
'''

MatchResult = collections.namedtuple(
    'MatchResult', ('winning_team', 'losing_team'))


def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)


matches = [
    MatchResult('Germany', 'Portugal'),
    MatchResult('France', 'Germany'),
    MatchResult('Portugal', 'Bulgaria'),
    MatchResult('France', 'Bulgaria'),
    MatchResult('Bulgaria', 'Germany'),
]

assert(can_team_a_beat_team_b(matches, 'Portugal', 'France') == False)
assert(can_team_a_beat_team_b(matches, 'France', 'Portugal') == True)
