# Four in a row task
import numpy as np
import matplotlib.pyplot as plt
import fiar_env

if __name__=="__main__":

    num_trials = 10
    env = fiar_env.Fiar()

    done = False

    map = np.int16(np.linspace(0, 4 * 9 - 1, 4 * 9).reshape(4, 9).T)
    map_taken = np.int16(np.linspace(0, 4 * 9 - 1, 4 * 9).reshape(4, 9).T)
    map_1d = np.int16(np.linspace(0, 4 * 9 - 1, 4 * 9)).tolist()

    while not done:
        action = env.render(mode="terminal")
        while True:
            action = np.random.randint(len(map_1d))
            action2d = np.where(map == action)
            action2d = (action2d[0][0], action2d[1][0])
            if map_taken[action2d] != -1:
                break
        map_taken[action2d] = -1
        env.player = 0
        state, reward, done, info = env.step(action2d)

        if env.game_ended():
            env.render(mode="terminal")
            print("*" * 20)
            print('Game ended! [' + ('WHITE' if np.all(env.state_[2] == 1) else 'BLACK') + '] won!')
            SWITCHERS, STRRS = fiar_env.fiar_check(env.state_, loc=True)
            print("*" * 20)
            print('winning streak: ', STRRS)
            print('\n')
            break
        action = env.render(mode="terminal")
        while True:
            action = np.random.randint(len(map_1d))
            action2d = np.where(map == action)
            action2d = (action2d[0][0], action2d[1][0])
            if map_taken[action2d] != -1:
                break

        env.player = 1
        map_taken[action2d] = -1
        state, reward, done, info = env.step(action2d)

        if env.game_ended():
            env.render(mode="terminal")
            print("*" * 20)
            print('Game ended! [' + ('WHITE' if np.all(env.state_[2] == 1) else 'BLACK') + '] won!')
            SWITCHERS, STRRS = fiar_env.fiar_check(env.state_, loc=True)
            print("*" * 20)
            print('winning streak: ', STRRS)
            print('\n')
            break

if __name__=="__main__human":
    num_trials = 10
    env = fiar_env.Fiar()

    done = False
    while not done:
        action = env.render(mode="human")
        state, reward, done, info = env.step(action)

        if env.game_ended():
            print("*" * 20)
            print('Game ended! [' + ('WHITE' if np.all(env.state_[2] == 1) else 'BLACK') + '] won!')
            break

        action = env.render(mode="human")
        state, reward, done, info = env.step(action)

        if env.game_ended():
            break

