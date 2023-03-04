# Project Proposal:
## Team
- Stephanie Georges
- Jack Sorenson
- Brock Brown

*We are using \*.md documents with the intent of diff tracking.*

## Abstract
We propose to build two separate robots to accomplish navigating the obstacle course, and drag racetrack. The first will be modularly constructed using both homemade components and 
some ordered from Adafruit and Amazon. The second will be a retro-fitted RC car with the RC module removed, and controlled via the STM32 Discovery board and accompanying peripherals. 
We realize our approach may seem a bit unorthodox, but feel we will meet the requirements set by the project, and retain the overarching goals of learning and having fun.

## [Parameters](proposal/parameters.md)
#### Important Assumptions (beyond what is mentioned in the challenge description):
- There will be time between the obstacle course & drag races to re-program & prepare the rover for each specific task.
- We will know the surface(s) the rover is expected to drive over _at least_ 3 weeks before rally (including start & end delineators).
  - We propose [this hyperlinked tape](https://a.co/d/b2FTbvO) to delineate start & end lines, and are willing to bring our own tape to implement it.
    - We would prefer distinct colors for [start](https://a.co/d/b2FTbvO) & [end](https://a.co/d/cOK2Wyo) lines.
- We will know definitive lighting conditions & their variance *at least* 3 weeks prior to the rally.
- The only obstacles will be cardboard boxes.
- Doors allowing unreasonable wind speeds into the course will be closed during rover's navigation.

#### Important Questions _(pertinent to obstacle course only)_:
- Will there be dead ends?
- What percentage of the course space will be covered by obstructions?

## [Bill of Materials](proposal/bom.md)

## [Milestones](proposal/milestones.md)

## Functionality
_Use at least 3 of the following:_
- Interrupts
  - The rotary encoders on the wheels will be handled with interrupts.
- PID
  - The power supplied to the wheels in the Obstacle Course Rover will be handled with PID.
- Analog
  - The light sensors & whiskers will use analog inputs over GPIO pins.
- UART
  - The collected training data will be communicated via wired UART.

## System Design Representation

### [Drag Race](proposal/drag-race-design-plan.md)

### [Obstacle Course](proposal/obstacle-course-design-plan.md)

## Incidentals
While our discussion of the potential problems with our design approach are peppered through the proposal, they are also summarized here.
- We may encounter problems with our homemade force sensors, or whiskers. In this case, we will order the replacements from Adafruit listed in the BoM.
- Securing the whiskers to our robot may be a bit challenging. We will attempt to use a staple for a clean application, but may have to do some less attractive duct taping.
- It may be too compute intensive to do both the light sensing and whisker sensing, in which case we will ditch the light sensing backup circuit.
- If the obstacle course contains many dead-ends on the left-hand side of the course, our rover may drain its batteries prior to completing the course.
- While our team has prior experience reprogramming an RC car, the workload associated with this approach may exceed our available time for completion. If this occurs, we will use our obstacle course rover instead.


