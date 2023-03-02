# Obstacle Course Approaches

## Left-Hand Rule
Rover first turns $90^o$ left, then follows start line until colliding with the wall, at which point the rover maintains contact on its left side with the wall until detection of end line.
### Complications:
- Rover will need $2+$ whiskers on its left side of differing lengths. one contact will indicate adequate proximity, two contacts will indicate excessive proximity to the wall. No contact will indicate inadequate proximity and the rover will turn left until contact is found.
- Rover will need to follow the start line, and be capable of distinguishing start & end lines.
- Rover _may_ depart from & return to start line in order to avoid a box placed on the start line.
- Brute-force method maximizes minimum course traversal time.

## Straight Shot Rule
Rover drives directly forward in whatever direction it has been placed until it encounters an obstacle. Once encountered, rover navigates around it, then returns to its initial direction.
### Complications:
- Need for accurate & precise directional awareness.
- Vulnerability to dead ends.

## Associated Sensors:
- Rotary Encoder on wheels
- Whiskers
- Light Sensors & Sources