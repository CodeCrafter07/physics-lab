import resources.physics as physics

simulator = physics.Simulator()
simulator.create_window()

ball = physics.Ball(simulator)

while simulator.running:
    if ball.shouldFollow:  # 2
        ball.follow_mouse()  # 2
    else:
        if ball.touching_ground() or ball.touching_walls():  # 3
            ball.bounce()

        ball.gravity()
        ball.stabilize()

    ball.move()

    simulator.update(ball)
