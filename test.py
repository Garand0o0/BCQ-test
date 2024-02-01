# # import os
# # # os.add_dll_directory('C:/Users/admin/.mujoco/mujoco200/bin')
# #
# # import mujoco_py
# #
# # mj_path,_= mujoco_py.utils.discover_mujoco()
# # xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
# # model = mujoco_py.load_model_from_path(xml_path)
# # sim = mujoco_py.MjSim(model)
# # print(sim.data.qpos)
# # sim.step()
# # print(sim.data.qpos)
#
#
#
# import gym
# env = gym.make("CartPole-v1") # 创建游戏环境
# observation = env.reset() # 游戏回到初始状态
# for _ in range(1000):
# 		env.render() # 显示当前时间戳的游戏画面
# 		action = env.action_space.sample() # 随机生成一个动作
# 		# 与环境交互，返回新的状态，奖励，是否结束标志，其他信息
# 		observation, reward, done, info = env.step(action)
# 		if done:#游戏回合结束，复位状态
# 				observation = env.reset()
# env.close()


# #开发者：Bright Fang
# #开发时间：2022/5/8 12:33
# import gym
# # import mujoco
# env = gym.make('Humanoid-v2')
# env = env.unwrapped
# for episode in range(20):
#     observation = env.reset() #环境重置
#     print(episode)
#     # for timestep in range(100):
#     while True:
#         # print(timestep)
#         env.render() #可视化
#         action = env.action_space.sample() #动作采样
#         observation_, reward, done, info = env.step(action) #单步交互
#         # if done:
#         #     # print(observation)
#         #     print('Episode {}'.format(episode))
#         #     break
#         observation=observation_
# env.close()


# 测试内容
print('test')

# 测试上传方式
print('test11')
