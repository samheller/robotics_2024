# Autonomous Strategies

This folder contains example autonomous strategies aimed at maximizing points in competition. Each strategy includes a brief description and a Python file that modifies `state_machine/version2.py` to implement the approach.

The examples are intentionally simple so you can adapt them to your own robot.

## Offensive Strategy

The offensive approach focuses on rapid target acquisition and aggressive scoring.

### Key Tactics

- **Fast Scan** – rotate quickly at the start to locate scoring objects.
- **Direct Approach** – drive at high speed once a target is detected.
- **Extended Attack** – run the arm mechanism longer to ensure the object is scored.

This strategy trades precision for speed. Tune the velocities based on how much room you have on the field.

## Defensive Strategy

The defensive approach focuses on blocking opponents and preventing them from scoring.

### Key Tactics

- **Slow Scan** – rotate carefully to keep the robot oriented toward incoming opponents.
- **Maintain Distance** – approach only far enough to block or push objects away.
- **Quick Retreat** – back up after each interaction to reset your position.

Use this strategy when protecting your scoring zones is more important than fast offense.

## Balanced Strategy

This approach mixes offensive scoring with periodic defensive maneuvers.

### Key Tactics

- **Moderate Scan Speed** – search for targets while staying aware of opponents.
- **Controlled Approach** – drive forward at a steady pace to maintain accuracy.
- **Short Attack Cycle** – limit the arm motion so the robot can quickly return to a neutral position.

The balanced strategy is useful when you need flexibility during a match.
