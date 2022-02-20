# Uses python3
import sys


def optimal_weight(W, w):
    return optimal_weight_dp(W, w)


def optimal_weight_recursion(W, w):

    def optimal_weight_inner(free_space, gold_bricks):
        free_spaces = []
        for i in range(0, len(gold_bricks)):
            gold_brick = gold_bricks[i]
            # print('gold brick: {}'.format(gold_brick))

            if free_space - gold_brick > 0 and len(gold_bricks) > 1:
                free_spaces.append(lambda gold_brick_copy=gold_brick, index=i: optimal_weight_inner(free_space - gold_brick_copy,
                                                                [gold_bricks[j] for j in range(0, len(gold_bricks)) if j != index]))
            elif free_space - gold_brick == 0:
                return 0
            else:
                free_spaces.append(free_space)

        free_spaces_clean = []
        for element in free_spaces:
            value = element
            if callable(value):
                value = value()
            free_spaces_clean.append(value)
        return min(free_spaces_clean)

    return W - optimal_weight_inner(W, w)

def optimal_weight_dp_v0(W, w):

    cache = {}

    def optimal_weight_dp_cache(free_space, gold_bricks):
        bricks_str = str(gold_bricks)
        if bricks_str in cache:
            return cache[bricks_str]
        value = optimal_weight_inner(free_space, gold_bricks)
        cache[bricks_str] = value
        return value

    def optimal_weight_inner(free_space, gold_bricks):
        free_spaces = [optimal_weight_dp_cache(free_space - gold_bricks[i],
                                               [gold_bricks[j] for j in range(0, len(gold_bricks)) if j != i])
                       if free_space - gold_bricks[i] >= 0 and len(gold_bricks) > 1 else free_space
                       for i in range(0, len(gold_bricks))]

        return min(free_spaces)

    w.sort(reverse=True)
    return W - optimal_weight_dp_cache(W, w)


def optimal_weight_dp(W, w):
    steps = [Step(Value(0), None)]
    item_values = [Value(item_weight) for item_weight in w]

    for k_weight_val in range(1, W+1):
        steps.append(None)
        k_weight = Value(k_weight_val)
        for item_weight in item_values:
            if item_weight <= k_weight:
                previous_step = steps[k_weight.value-item_weight.value]
                if previous_step is not None and not previous_step.contains(item_weight):
                    potential_current_step = Step(item_weight, previous_step)
                    if steps[k_weight.value] is None or steps[k_weight.value].get_total_value() < potential_current_step.get_total_value():
                        steps[k_weight.value] = potential_current_step

    for index in range(len(steps)-1, -1, -1):
        if steps[index] is not None:
            return steps[index].get_total_value().value

    return 0


class Value:

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value


class Step:
    def __init__(self, value, previous_step) -> None:
        super().__init__()
        self.value = value
        self.previous_step = previous_step

    def contains(self, value):
        return self.value == value or (self.previous_step is not None and self.previous_step.contains(value))

    def get_total_value(self):
        def get_total_value_inner(step):
            if step.previous_step is None:
                return step.value.value
            return step.value.value + get_total_value_inner(step.previous_step)
        return Value(get_total_value_inner(self))


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
