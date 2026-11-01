# Shared standards

Keep generic design patterns and artifact templates in the public skill. Enterprise architecture decisions, approved technologies, constraints and the platform component catalog belong in an authorized enterprise repository, separate from this public skill and project specifications. Locate the enterprise repository once when needed and record its location in the project checkpoint; never hardcode enterprise URLs or copy private content into the public repository. Work without enterprise access by marking standards and platform choices unverified, never inventing them.

When designing, consult relevant enterprise standards and platform catalog entries on demand; distinguish mandated decisions from available platform options and open design choices. Do not copy the catalog into project artifacts unnecessarily.

For intake:
1. Read the supplied source and the relevant existing entries only.
2. Draft the smallest reusable rule with ID, status, scope, rule, rationale, source, version/effective date and exceptions.
3. Identify overlap, conflicts and affected approved rules. Present a proposed add, update or retirement for explicit architect approval.
4. Persist only approved library changes. Keep unapproved proposals distinct.
5. Apply approved rules automatically within scope and record their ID/path and version in project decisions/checkpoints. Do not ask the same question for the same approved pattern.
6. Surface contradictory or changed standards and identify affected artifacts before revision. Never silently replace a project decision.

No technology is pre-approved by this package. REST Python, OAuth, messaging bus and orchestration patterns become defaults only when the architect supplies or approves their actual rules. Preserve company-specific standards in their authorized location, outside this public repository.
