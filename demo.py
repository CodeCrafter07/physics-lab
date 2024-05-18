import resources.physics as physics

simulator = physics.Simulator()
simulator.create_window()

ball = physics.Ball(simulator, simulator.height)

while simulator.running:
    if ball.shouldFollow:
        ball.follow_mouse()
    else:
        if ball.touching_ground() or ball.touching_walls():
            ball.bounce()

        ball.gravity()
        ball.stabilize()

    ball.move()

    simulator.update(ball)
