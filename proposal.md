# Project Proposal:
**Lead:** Stephanie Georges
- Jack Sorenson
- Brock Brown

*We are using \*.md documents with the intent of diff tracking. The \*.html docs are products of the \*.md docs and can be used to more easily read our documentation.*

## [Parameters](proposal/parameters.md)
_The parameters document contains more specific information, but the above is information required as soon as possible._
#### Important Assumptions (beyond what is mentioned in the challenge description):
- There will be time between the obstacle course & drag races to re-program & prepare the rover for each specific task.
- We will know the surface(s) the rover is expected to drive over _at least_ 3 weeks before rally (including start & end delineators).
  - We propose [this hyperlinked tape](https://a.co/d/b2FTbvO) to delineate start & end lines, and are willing to bring our own tape to implement it.
    - We would prefer distinct colors for [start](https://a.co/d/b2FTbvO) & [end](https://a.co/d/cOK2Wyo) lines.
- We will know definitive lighting conditions & their variance *at least* 3 weeks prior to the rally.
- The only obstacles will be cardboard boxes.
- Doors allowing unreasonable wind speeds into the course will be closed during rover's navigation.

Important Questions _(pertinent to obstacle course only)_:
- Will there be dead ends?
- What percentage of the course space will be covered by obstructions?
- Can we build two separate rovers, one for each task?

## [Bill of Materials](proposal/bom.md)

## [Milestones](proposal/milestones.md)

## Functionality
_Use at least 3 of the following:_
- Interrupts
  - The rotary encoders on the wheels will be handled with interrupts.
- PID
  - The power supplied to the wheels in the Obstacle Course Rover will be handled with PID
- Analog
  - The light sensors & whiskers will use analog inputs over GPIO pins
- UART
  - The collected training data will be communicated via wired UART

## System Design Representation

### [Drag Race](proposal/drag-race-design-plan.md)

### [Obstacle Course](proposal/obstacle-course-design-plan.md)



