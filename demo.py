import Physics

simulator = Physics.Simulator()
simulator.create_window()

ball = Physics.Ball(simulator, simulator.height)

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
