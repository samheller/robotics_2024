# Balanced Strategy

This approach mixes offensive scoring with periodic defensive maneuvers.

## Key Tactics

- **Moderate Scan Speed** – search for targets while staying aware of opponents.
- **Controlled Approach** – drive forward at a steady pace to maintain accuracy.
- **Short Attack Cycle** – limit the arm motion so the robot can quickly return to a neutral position.

The balanced strategy is useful when you need flexibility during a match.

## State Flow

1. **Manual** – driver control of movement and the arm.
2. **Scanning** – moderate turning speed to locate objects while watching for
   opponents.
3. **Aligning** – short rotation to face the detected object before moving in.
4. **Approaching** – drive forward carefully until the object is in range.
5. **Attacking** – run the arm just long enough to score.
6. **Retreating** – back away and return to manual control.
