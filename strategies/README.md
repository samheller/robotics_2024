# Autonomous Strategies

This folder contains example autonomous tactics built on `state_machine/version2.py`.
The four strategies vary scanning speed, approach velocity and attack time.
Together they illustrate how these elements form a simple Nash equilibrium
between aggressive and defensive play.

## Strategies

1. **Offensive** – fast scan, direct approach and long attack cycle.
2. **Defensive** – slow scan, short approach and quick retreat.
3. **Balanced** – moderate parameters to stay flexible.
4. **Equilibrium** – values tuned near the predicted Nash equilibrium for
   opponents using mixed strategies.

Each subfolder provides a `.md` description and a matching Python file you can
adapt to your own robot.
