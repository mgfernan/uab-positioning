# Application design studio

This session guides you through designing an application that uses positioning.
Based on what you have learned in the course, you will:

- identify a user's needs;
- translate those needs into requirements; and
- design a solution that addresses those requirements.

By the end of the session, you should be able to present an application design
that could be implemented using available equipment and services, and explain
the evidence and assumptions behind your design.

## Preliminary work

**Before the session**, spend about 30 minutes on the following tasks:

1. **Review the course material**, in particular:
   - applications and use cases from the course introduction;
   - GNSS receiver types and their characteristics; and
   - added-value services.

2. **Form a team** of 2–3 people. You will work together throughout the session.

3. **Choose an application.** Select one from the examples at the end of this
   document, or propose your own. Keep it focused on one user, one task, and one
   operating environment. Come prepared to discuss:
   - Who is the user?
   - What decision or action does the user need positioning to support?
   - What constraints apply (for example, budget, operating environment,
     architecture, or hardware)?

4. **Find one possible receiver.** Search for one receiver that might suit your
   application. Bring its model name and a link to the manufacturer's datasheet
   or official technical specification. This is a starting candidate, not a
   final choice. If you cannot find a suitable specification, note what you
   searched for and where you got stuck. You can start with the receiver
   examples at the end of this document.

5. **Optional:** Read the rest of this document to preview the design steps and
   questions.

## A note on AI usage

AI use is encouraged for brainstorming, critique, explanation, and search support; but students remain responsible for the design. Technical and market claims will need verifiable sources; and each team will have to explain at least one AI-assisted decision, if they used it in their design.

## Session structure

Work through the steps below with your team. Use the questions and checklists to keep the design focused.

By the end, your team should have a one-page design brief or single slide with:

- the chosen use case and 4–6 prioritized requirements;
- a comparison of two receiver candidates, with evidence from their
  specifications;
- the selected receiver and any needed antenna, correction service, or other
  components;
- one important limitation and a fallback plan; and
- the intended user, payer, and value of the solution.

## Step 1: Identify user needs

- Narrow down the target user group: who will use the application?
- Identify the user's need: what decision or action will positioning support?
- Translate the need into positioning requirements. Consider accuracy,
  availability, integrity, update rate, latency, coverage, and cost.
- Record each requirement in a table with an ID, a measurable statement, its
  rationale, the operating conditions, and how it could be verified.

When writing requirements, make them:

- **Quantifiable:** Each requirement should be measurable and testable. State relevant operating conditions and a threshold or target.
- **Atomic:** Each requirement should express one obligation. Split a statement that combines independent measures or functions into separate requirements.

Examples of good and bad requirements:

| Quality | Bad example | Better example |
|---------|-------------|----------------|
| **Quantification** | “The receiver shall provide accurate positions.” | “Under open-sky conditions, horizontal position error shall be no greater than 5 m for at least 95% of epochs in a 30-minute test.” |
| **Atomicity** | “The receiver shall provide positions at 1 Hz and keep horizontal error below 5 m.” | Split it into two requirements: **(1)** “The receiver shall output a position solution at least once per second.” **(2)** “Under open-sky conditions, horizontal position error shall be no greater than 5 m for at least 95% of epochs in a 30-minute test.” |
| **Both** | “The receiver shall work reliably and quickly in challenging environments.” | Write separate measurable requirements for the relevant performance, such as solution availability, update rate, and time to produce a solution. State the operating conditions for each. |

Use this table to record your requirements. Add one row for each atomic requirement.

| ID | Requirement | User need it addresses | Operating conditions | How to verify it |
|----|-------------|------------------------|----------------------|------------------|
| REQ-01 | ... | ... | ... | ... |

## Step 2: Design the solution

Use the requirements from Step 1 to design a solution.

1. **Map requirements to capabilities.** Identify which GNSS capabilities and
   added-value services could address each requirement. Note any requirement
   that GNSS alone may not satisfy.

2. **Find and compare two receiver candidates.** Search for receivers that
   could suit your application. For each candidate, find the manufacturer's
   datasheet or official technical specification and record the model name,
   source link, and the relevant page or section. Compare the candidates on the
   properties that matter to your requirements:
   - supported constellations and frequency bands;
   - positioning modes and stated accuracy, including the conditions for that
     accuracy (for example, standalone, SBAS, RTK, or PPP, if applicable);
   - correction-service compatibility;
   - position output rate and interfaces;
   - power, size, and antenna requirements; and
   - cost, if reliable pricing is available.

   Use a comparison table to keep the search focused. Include a source link and
   page or section for each specification you use.

   | Requirement or property | Candidate A: value and source | Candidate B: value and source | Fit or open question |
   |--------------------------|------------------------------|------------------------------|----------------------|
   | Positioning accuracy and conditions | ... | ... | ... |
   | Constellations and bands | ... | ... | ... |
   | Correction services and interfaces | ... | ... | ... |
   | Update rate and output interface | ... | ... | ... |
   | Power, size, antenna, or cost (as relevant) | ... | ... | ... |

   For each requirement, mark the evidence as **supported**, **not supported**,
   or **unclear** based on the published specifications. Do not treat a headline
   accuracy figure as proof unless its conditions match your use case. If a
   specification is missing or ambiguous, record it as unknown and say how you
   would test it.

3. **Select and justify a receiver.** Choose one candidate and explain why it
   fits better than the alternative. Consider whether you also need a separate
   antenna, correction service, or other added-value service. You may include
   complementary sensors such as an IMU or barometer.

4. **Plan for failure or degraded performance.** What happens if GNSS signals
   are lost, inaccurate, or unavailable? Explain how the application should
   behave and identify a fallback, if one is needed.

## Step 3: Rapid market check

This is a short scan to identify the likely user, payer, value, and an
alternative. It is not a full market analysis.

Refine the proposal as a product or service. Keep the research focused:

- Who benefits from the solution?
- Who pays for it? The user and the paying customer may be different.
- What pain point does the solution address, and what value does it provide?
- What alternative product, service, or non-GNSS method does the user have?
- What trade-offs or barriers could affect adoption (for example, cost,
  coverage, integration, regulation, or user trust)?

Find at least one source about a comparable product, service, or alternative.
Record the source and distinguish sourced information from your own estimates
or assumptions.

## Step 4: Elevator pitch

Prepare a **one-minute pitch** to present your idea to the rest of the class.
Cover:

1. the user and the problem;
2. your proposed solution, including the receiver or service you selected;
3. the strongest evidence that it meets the main requirements; and
4. one important limitation and how you would address it.

## Example use cases and applications

Use these examples for inspiration. Narrow your choice to one user, one task,
and one operating environment before you start the design.

- **Agriculture:** precision farming, crop monitoring, or livestock tracking.
- **Construction:** machine control, site surveying, or asset tracking.
- **Transportation:** fleet management, navigation, or traffic monitoring.
- **Emergency services:** search and rescue, disaster response, or emergency
  vehicle tracking.
- **Environmental monitoring:** wildlife tracking, pollution monitoring, or
  field data collection.
- **Sports and recreation:** outdoor activity tracking, adventure tourism, or
  geocaching.
- **Healthcare:** patient monitoring, medical equipment tracking, or telemedicine.
- **Smart cities:** smart parking, public transport tracking, or urban planning.
- **Retail and logistics:** inventory management, delivery tracking, or supply
  chain management.
- **Security and surveillance:** perimeter monitoring, asset protection, or
  crowd management.

## Example of GNSS receivers

These examples span different performance classes and are starting points, not
like-for-like candidates. Compare equipment that could plausibly meet the same
use-case requirements.

- **u-blox ZED-X20K:** A multi-constellation module that supports GPS, GLONASS, Galileo, and BeiDou. [ZED-X20K series and datasheet](https://www.u-blox.com/en/product/zed-x20k-module). Find other models in the [u-blox product selector](https://www.u-blox.com/en/product-selector).
- **ArduSimple SimpleRTK2B:** A compact RTK GNSS receiver that supports GPS, GLONASS, Galileo, and BeiDou. It provides centimeter-level accuracy when used with a base station or correction service. [Datasheet link](https://www.ardusimple.com/product/simplertk2b/). You can also find alternative receivers in the [ArduSimple web page](https://www.ardusimple.com/)
- **Trimble R980:** A high-precision GNSS receiver designed for professional surveying and mapping applications. It supports multiple constellations and offers advanced features for accurate positioning. [Datasheet link](https://geospatial.trimble.com/en/products/hardware/trimble-r980).
- **NovAtel** receivers: browse the [NovAtel product catalog](https://novatel.com/products/receivers).

## References

- [EUSPA Market report 2026](https://www.euspa.europa.eu/sites/default/files/documents/EU_Space_Market_Report_2026.pdf)
