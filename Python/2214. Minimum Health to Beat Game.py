# You may use your armor ability at most once during the game on any level which will protect you from at most armor damage.
# You must complete the levels in order and your health must be greater than 0 at all times to beat the game.
# Return the minimum health you need to start with to beat the game.

# O(N), O(1)
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        min_health = sum(damage) + 1
        if max_damage <= armor:
            min_health -= max_damage
        elif max_damage > armor: 
            min_health -= armor
        return min_health


class Solution2:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage_prevented = min(max(damage), armor)
        return sum(damage) + 1 - max_damage_prevented
