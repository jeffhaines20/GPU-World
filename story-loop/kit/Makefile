.PHONY: checks plant-faults calibrate claims gate decide intake

checks:
	python3 checks/run_all_checks.py

plant-faults:
	python3 checks/plant_faults.py

claims:
	python3 checks/check_claims.py

calibrate:
	python3 checks/calibrate.py

# The human's paragraph at a gate. They write it; no agent writes it for them. G3 asks a different
# question from the others: it is the first reading of a draft, not a decision, so it does not ask
# whether the story goes through.
gate:
	@echo "Gate G$(N). Read what INBOX.md asks you to read, then, in DECISIONS.md, under '## Gate sign-offs',"
	@echo "add a section:"
	@echo ""
	@echo "  ### G$(N) — $$(date +%Y-%m-%d)"
	@echo ""
	@if [ "$(N)" = "3" ]; then \
	  echo "  <three to five sentences in your own words: what you felt reading it, what stayed with you,"; \
	  echo "   and what must change>"; \
	  echo ""; \
	  echo "This gate asks what the draft did to you, not whether it goes through: revision rounds continue"; \
	  echo "either way, and everything you say becomes findings the revisions have to answer."; \
	else \
	  echo "  <three to five sentences in your own words: what you saw, what you liked, what must change,"; \
	  echo "   whether it goes through>"; \
	fi
	@echo ""
	@echo "Save the file. That paragraph is yours and is never edited afterwards."

# A decision row. Most types are the human's and they write the row themselves; routing is the
# orchestrator's own record of how it spawns agents, so the printed author follows the type.
decide:
	@echo "Decision of type $(TYPE)  (pick, caps, title, taste, routing, gate-amend, fault-suite, other)."
	@echo "In DECISIONS.md, add a row to the table:"
	@echo ""
	@if [ "$(TYPE)" = "routing" ]; then \
	  echo "  | DEC-NNN | $$(date +%Y-%m-%d) | agent | routing | <which sub-agent facility this project uses> | <why> | <what you did not choose> |"; \
	  echo ""; \
	  echo "This is the one type the orchestrator writes: it records how agents are spawned here, which is"; \
	  echo "the agent's own fact about its harness, not a choice the human makes. Author is 'agent'."; \
	else \
	  echo "  | DEC-NNN | $$(date +%Y-%m-%d) | human | $(TYPE) | <what you decided> | <why> | <what you did not choose> |"; \
	  echo ""; \
	  echo "This row is yours: no agent may write it, and 'caps', 'gate-amend' and 'fault-suite' rows are"; \
	  echo "checked for the human author, because each one unlocks something the checks otherwise refuse."; \
	fi
	@echo ""
	@echo "Use the next free DEC number. Save the file."

# The end of intake: the human commits the brief and the caps they accepted.
intake:
	@echo "In the project folder, as yourself (the agents never run this for you):"
	@echo "  git add BRIEF.md checks/caps.approved.json && git commit -m 'Intake'"
	@echo "(If this project is not in git, save both files and tell the orchestrator they are final.)"
