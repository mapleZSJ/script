import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--times", type=int, default=100000, help="times to get the final reward")
args = parser.parse_args()

def simulate_draws(num_simulations):
    initial_probability = 0.006
    max_probability = 0.216
    increase_rate = 0.06
    guaranteed_draw_60 = 60
    guaranteed_draw_90 = 90
    total_draws_to_get_itemA = 0
    total_to_get_itemA = 0

    for _ in range(num_simulations):
        probability = initial_probability
        draws = 0
        consecutive_draws = 0
        consecutive_draws_without_A = 0

        while True:
            draws += 1
            consecutive_draws += 1
            consecutive_draws_without_A += 1
            
            # 第90次必定获得道具A
            if consecutive_draws_without_A == guaranteed_draw_90:
                total_draws_to_get_itemA += draws
                total_to_get_itemA += 1
                print(f"1：获得道具A的次数是：{total_to_get_itemA}次，抽奖次数是：{draws}")
                break

            # 判断是否抽中大礼包1：
            if random.random() < probability:
                # 判断是否获得道具A
                if random.random() < 0.3:
                    total_draws_to_get_itemA += draws
                    total_to_get_itemA += 1
                    print(f"2：获得道具A的次数是：{total_to_get_itemA}次，抽奖次数是：{draws}")
                    break
                else:
                    # 抽中大礼包但未获得道具A，重置概率和连续未中次数
                    probability = initial_probability
                    consecutive_draws = 0
            elif consecutive_draws == guaranteed_draw_60:
                # 第60次必定获得大礼包
                if random.random() < 0.3:
                    total_draws_to_get_itemA += draws
                    total_to_get_itemA += 1
                    print(f"3：获得道具A的次数是：{total_to_get_itemA}次，抽奖次数是：{draws}")
                    break
                # 重置概率和连续未中次数
                probability = initial_probability
                consecutive_draws = 0
            else:
                if consecutive_draws > 41:
                    probability = min(probability + increase_rate, max_probability)
                # 41次抽卡之后，概率按每次增加6%计算

    expected_draws_to_get_itemA = total_draws_to_get_itemA / total_to_get_itemA
    return expected_draws_to_get_itemA, total_to_get_itemA

expected_draws_to_get_itemA, total_to_get_itemA = simulate_draws(args.times)
print(f"获得道具A的期望抽数是：{expected_draws_to_get_itemA:.2f}次")
print(f"获得道具A的次数是：{total_to_get_itemA}次")
