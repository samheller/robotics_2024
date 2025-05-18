# Autonomous Strategies

This folder contains example autonomous strategies aimed at maximizing points in competition.
Each strategy includes a brief description and a Python file that modifies
`state_machine/version2.py` to implement the approach.

The examples are intentionally simple so you can adapt them to your own robot.

Each strategy now uses a six-state machine:

1. **Manual** – default driver control.
2. **Scanning** – rotate to look for game pieces.
3. **Aligning** – make a small turn to face the target.
4. **Approaching** – drive forward until the object is close.
5. **Attacking** – move the arm to score or block.
6. **Retreating** – back away and return to manual control.
