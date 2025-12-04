# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= python3 -m sphinx
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean html api

# Clean build artifacts
clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(SOURCEDIR)/api_reference/modules.rst
	find $(SOURCEDIR)/api_reference -name "*.rst" ! -name "index.md" -type f -delete

# Build HTML documentation
html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Generate API documentation using sphinx-apidoc
api:
	@command -v sphinx-apidoc >/dev/null 2>&1 && sphinx-apidoc -o $(SOURCEDIR)/api_reference -f -e ../ || python3 -m sphinx.ext.apidoc -o $(SOURCEDIR)/api_reference -f -e ../
	@echo "API documentation generated in $(SOURCEDIR)/api_reference/"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
