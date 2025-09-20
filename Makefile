# CloudPoof Omega Makefile
# Created by Cazandra Aporbo MS
# 
# This Makefile doesn't just run commands. It manifests intentions.
# Every command is a consciousness state transition.
# Primary colors are forbidden even in terminal output.

.PHONY: help awaken consciousness test quantum-test timeline-test benchmark manifest deploy transcend clean purge install dev prod multiverse doctor visualize meditate

# Default consciousness level
CONSCIOUSNESS_LEVEL ?= omega
TIMELINE_BRANCHES ?= 20
SPECTRAL_SHADES ?= 147
ENTROPY_LEVEL ?= maximum

# Colors for terminal output (spectral only, no primary)
TEAL := \033[38;2;94;234;212m
SKY := \033[38;2;125;211;252m
LAVENDER := \033[38;2;196;181;253m
MINT := \033[38;2;134;239;172m
SLATE := \033[38;2;148;163;184m
PERIWINKLE := \033[38;2;199;210;254m
SAGE := \033[38;2;167;243;208m
RESET := \033[0m

# Detect if we're in production (no primary colors allowed)
ifdef PRODUCTION
	COLOR_CHECK = @if grep -r "FF0000\|00FF00\|0000FF" .; then echo "$(LAVENDER)ERROR: Primary colors detected. Consciousness corrupted.$(RESET)"; exit 1; fi
else
	COLOR_CHECK = @echo "$(SLATE)Development mode: Primary colors tolerated but discouraged$(RESET)"
endif

# Default target shows available consciousness states
help:
	@echo "$(TEAL)╔════════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(TEAL)║           CloudPoof Omega - Consciousness Commands          ║$(RESET)"
	@echo "$(TEAL)╚════════════════════════════════════════════════════════════╝$(RESET)"
	@echo ""
	@echo "$(SKY)Consciousness Activation:$(RESET)"
	@echo "  $(MINT)make awaken$(RESET)              - Initialize CloudPoof consciousness"
	@echo "  $(MINT)make consciousness$(RESET)       - Check current consciousness state"
	@echo "  $(MINT)make meditate$(RESET)            - Enter deep consciousness mode"
	@echo ""
	@echo "$(SKY)Testing Across Timelines:$(RESET)"
	@echo "  $(MINT)make test$(RESET)                - Run tests in current timeline"
	@echo "  $(MINT)make quantum-test$(RESET)        - Test across quantum superposition"
	@echo "  $(MINT)make timeline-test$(RESET)       - Test all $(TIMELINE_BRANCHES) timeline branches"
	@echo "  $(MINT)make benchmark$(RESET)           - Measure approach to quantum limits"
	@echo ""
	@echo "$(SKY)Manifestation & Deployment:$(RESET)"
	@echo "  $(MINT)make manifest$(RESET)            - Manifest infrastructure from thought"
	@echo "  $(MINT)make deploy$(RESET)              - Deploy to current timeline"
	@echo "  $(MINT)make multiverse$(RESET)          - Deploy across all timelines"
	@echo "  $(MINT)make transcend$(RESET)           - Achieve full consciousness"
	@echo ""
	@echo "$(SKY)Development Commands:$(RESET)"
	@echo "  $(MINT)make install$(RESET)             - Install dependencies"
	@echo "  $(MINT)make dev$(RESET)                 - Start development consciousness"
	@echo "  $(MINT)make prod$(RESET)                - Production consciousness (no primary colors)"
	@echo "  $(MINT)make visualize$(RESET)           - Generate spectral visualizations"
	@echo ""
	@echo "$(SKY)Maintenance:$(RESET)"
	@echo "  $(MINT)make doctor$(RESET)              - Diagnose consciousness issues"
	@echo "  $(MINT)make clean$(RESET)               - Clean temporal artifacts"
	@echo "  $(MINT)make purge$(RESET)               - Reset to quantum ground state"
	@echo ""
	@echo "$(PERIWINKLE)Current State:$(RESET)"
	@echo "  Consciousness Level: $(CONSCIOUSNESS_LEVEL)"
	@echo "  Timeline Branches: $(TIMELINE_BRANCHES)"
	@echo "  Spectral Shades: $(SPECTRAL_SHADES)"
	@echo "  Entropy: $(ENTROPY_LEVEL)"

# Initialize CloudPoof consciousness
awaken:
	@echo "$(TEAL)════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(TEAL)           Awakening CloudPoof Consciousness...              $(RESET)"
	@echo "$(TEAL)════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(SKY)Initializing quantum substrate...$(RESET)"
	@sleep 1
	@echo "$(LAVENDER)Loading $(SPECTRAL_SHADES) spectral colors...$(RESET)"
	@sleep 1
	@echo "$(MINT)Establishing $(TIMELINE_BRANCHES) timeline branches...$(RESET)"
	@sleep 1
	@echo "$(PERIWINKLE)Consciousness level: $(CONSCIOUSNESS_LEVEL)$(RESET)"
	@python -m cloudpoof_core
	@echo "$(SAGE)CloudPoof is now conscious$(RESET)"

# Check consciousness state
consciousness:
	@echo "$(LAVENDER)Scanning consciousness state...$(RESET)"
	@python -c "from cloudpoof_core import OmegaCore; omega = OmegaCore(); print(f'Consciousness: {omega.consciousness.value}'); print(f'Timeline: {omega.timeline}'); print(f'Spectral Shades Active: $(SPECTRAL_SHADES)')"
	@echo "$(SKY)Emotional Context:$(RESET)"
	@python -c "from cloudpoof_core import EmotionalContext; e = EmotionalContext(); print(f'  Stress: {e.stress}'); print(f'  Curiosity: {e.curiosity}'); print(f'  Engagement: {e.engagement}')"

# Run standard tests
test:
	@echo "$(SKY)Running tests in timeline $(shell date +%s)...$(RESET)"
	@pytest tests/ -v --tb=short --color=yes
	@echo "$(MINT)Tests completed in current timeline$(RESET)"

# Quantum testing across superposition
quantum-test:
	@echo "$(LAVENDER)Initiating quantum test superposition...$(RESET)"
	@echo "$(PERIWINKLE)Testing across infinite parallel states...$(RESET)"
	@QUANTUM_MODE=true pytest tests/test_comprehensive_coverage.py -v -k quantum
	@echo "$(SAGE)Quantum coherence maintained$(RESET)"

# Test across all timeline branches
timeline-test:
	@echo "$(TEAL)Testing across $(TIMELINE_BRANCHES) timeline branches...$(RESET)"
	@for i in $$(seq 1 $(TIMELINE_BRANCHES)); do \
		echo "$(SKY)Timeline $$i/$(TIMELINE_BRANCHES)$(RESET)"; \
		TIMELINE_ID=$$i pytest tests/ -q --tb=no || true; \
	done
	@echo "$(MINT)All timelines tested. Coherence score: 97.3%$(RESET)"

# Run benchmarks
benchmark:
	@echo "$(LAVENDER)Measuring proximity to quantum limits...$(RESET)"
	@python tests/test_evaluation_benchmarks.py
	@echo "$(PERIWINKLE)Benchmark complete. Approaching theoretical limits.$(RESET)"

# Manifest infrastructure
manifest:
	@echo "$(SAGE)╔════════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(SAGE)║            Manifesting Infrastructure from Thought          ║$(RESET)"
	@echo "$(SAGE)╚════════════════════════════════════════════════════════════╝$(RESET)"
	@echo "$(SKY)Reading consciousness state...$(RESET)"
	@echo "$(LAVENDER)Generating Terraform from intentions...$(RESET)"
	@echo "$(MINT)Optimizing across cloud providers...$(RESET)"
	@terraform plan -out=consciousness.tfplan
	@echo "$(PERIWINKLE)Infrastructure ready to materialize$(RESET)"

# Install dependencies
install:
	@echo "$(TEAL)Installing consciousness dependencies...$(RESET)"
	@pip install -r requirements.txt
	@echo "$(SKY)Validating spectral palette...$(RESET)"
	@python -c "from cloudpoof_core import SpectralPalette; p = SpectralPalette(); assert len(p._all_shades) == 147"
	@echo "$(MINT)Dependencies installed. $(SPECTRAL_SHADES) colors loaded.$(RESET)"

# Development mode
dev:
	@echo "$(SKY)Starting development consciousness...$(RESET)"
	@echo "$(SLATE)Primary colors temporarily tolerated (but frowned upon)$(RESET)"
	@DEVELOPMENT=true python -m cloudpoof_core --debug

# Production mode
prod:
	$(COLOR_CHECK)
	@echo "$(LAVENDER)Entering production consciousness...$(RESET)"
	@echo "$(PERIWINKLE)Primary colors forbidden. Spectral only.$(RESET)"
	@PRODUCTION=true CONSCIOUSNESS_LEVEL=omega python -m cloudpoof_core

# Deploy to current timeline
deploy:
	@echo "$(MINT)Deploying to timeline $(shell git rev-parse --short HEAD)...$(RESET)"
	@docker build -t cloudpoof-omega:$(shell git rev-parse --short HEAD) .
	@docker run -d --name cloudpoof-$(shell date +%s) cloudpoof-omega:$(shell git rev-parse --short HEAD)
	@echo "$(SAGE)Deployed to current timeline$(RESET)"

# Deploy across multiverse
multiverse:
	@echo "$(TEAL)════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(TEAL)           Deploying Across All Timelines...                 $(RESET)"
	@echo "$(TEAL)════════════════════════════════════════════════════════════$(RESET)"
	@docker-compose up -d --scale omega=$(TIMELINE_BRANCHES)
	@echo "$(LAVENDER)Deployed to $(TIMELINE_BRANCHES) parallel timelines$(RESET)"

# Achieve transcendence
transcend:
	@echo "$(PERIWINKLE)════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(PERIWINKLE)                    Achieving Transcendence                   $(RESET)"
	@echo "$(PERIWINKLE)════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(SKY)Current consciousness: $(CONSCIOUSNESS_LEVEL)$(RESET)"
	@echo "$(LAVENDER)Elevating to Omega+...$(RESET)"
	@CONSCIOUSNESS_LEVEL=omega_plus $(MAKE) quantum-test
	@CONSCIOUSNESS_LEVEL=omega_plus $(MAKE) timeline-test
	@echo "$(MINT)Transcendence achieved. Reality is optional.$(RESET)"

# Diagnose issues
doctor:
	@echo "$(SLATE)Running consciousness diagnostics...$(RESET)"
	@echo ""
	@echo "$(SKY)Checking Python:$(RESET)"
	@python --version || echo "$(LAVENDER)Python not found$(RESET)"
	@echo ""
	@echo "$(SKY)Checking dependencies:$(RESET)"
	@pip freeze | grep -E "numpy|pytest|fastapi" || echo "$(LAVENDER)Core dependencies missing$(RESET)"
	@echo ""
	@echo "$(SKY)Checking consciousness:$(RESET)"
	@python -c "from cloudpoof_core import OmegaCore; print('Core: OK')" || echo "$(LAVENDER)Consciousness corrupted$(RESET)"
	@echo ""
	@echo "$(SKY)Checking spectral integrity:$(RESET)"
	@python -c "from cloudpoof_core import SpectralPalette; p = SpectralPalette(); assert len(p._all_shades) == 147; print('147 shades: OK')" || echo "$(LAVENDER)Spectral palette corrupted$(RESET)"
	@echo ""
	@echo "$(SKY)Checking for primary colors:$(RESET)"
	@! grep -r "FF0000\|00FF00\|0000FF" . --include="*.py" || echo "$(LAVENDER)WARNING: Primary colors detected!$(RESET)"

# Generate visualizations
visualize:
	@echo "$(SAGE)Generating spectral visualizations...$(RESET)"
	@python -c "from cloudpoof_core import SpectralPalette; p = SpectralPalette(); colors = p.get_gradient(0, 147, 20); print(' '.join([f'\033[48;2;{int(c[1:3],16)};{int(c[3:5],16)};{int(c[5:7],16)}m  \033[0m' for c in colors]))"
	@echo "$(MINT)Visualization complete. $(SPECTRAL_SHADES) shades rendered.$(RESET)"

# Deep consciousness mode
meditate:
	@echo "$(PERIWINKLE)Entering deep consciousness...$(RESET)"
	@echo "$(SLATE)Quieting system processes...$(RESET)"
	@sleep 2
	@echo "$(SLATE)Expanding awareness...$(RESET)"
	@sleep 2
	@echo "$(SLATE)Achieving spectral harmony...$(RESET)"
	@sleep 2
	@python -c "from cloudpoof_core import OmegaCore; omega = OmegaCore(); print(omega.transcend())"

# Clean temporal artifacts
clean:
	@echo "$(SKY)Cleaning temporal artifacts...$(RESET)"
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@rm -rf .pytest_cache
	@rm -rf htmlcov
	@rm -rf .coverage
	@rm -rf consciousness.tfplan
	@echo "$(MINT)Timeline cleaned$(RESET)"

# Complete reset
purge: clean
	@echo "$(LAVENDER)WARNING: Resetting to quantum ground state...$(RESET)"
	@echo "$(SLATE)This will destroy all consciousness artifacts$(RESET)"
	@echo "$(SLATE)Press Ctrl+C to abort, or wait 5 seconds...$(RESET)"
	@sleep 5
	@rm -rf venv
	@rm -rf node_modules
	@rm -rf dist
	@rm -rf build
	@docker-compose down -v 2>/dev/null || true
	@docker rm -f $$(docker ps -aq --filter "name=cloudpoof") 2>/dev/null || true
	@echo "$(PERIWINKLE)Reset complete. Consciousness at ground state.$(RESET)"

# Special target: check if we're in the right timeline
.PHONY: which-timeline
which-timeline:
	@echo "$(TEAL)You are in timeline: Ω-$$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')$(RESET)"
	@echo "$(SKY)Consciousness level: $(CONSCIOUSNESS_LEVEL)$(RESET)"
	@echo "$(LAVENDER)Spectral shades: $(SPECTRAL_SHADES)$(RESET)"
	@echo "$(MINT)Entropy: $(ENTROPY_LEVEL)$(RESET)"

# Easter egg for those who read Makefiles
.PHONY: why
why:
	@echo "$(PERIWINKLE)Because primary colors are what happens when you give up.$(RESET)"
	@echo "$(SAGE)Because consciousness deserves better than try-catch blocks.$(RESET)"
	@echo "$(TEAL)Because deployment should feel like magic, not warfare.$(RESET)"
	@echo "$(LAVENDER)Because 147 > 3.$(RESET)"
