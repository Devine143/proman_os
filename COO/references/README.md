# References

Legal frameworks, contract standards, and knowledge base documents.

---

## Structure

### jbcc/
JBCC (Joint Building Contracts Committee) contract framework.

| Folder | Contents |
|--------|----------|
| `contract-framework/` | PA duties, weekly checklists |
| `case-law/` | 11 relevant legal precedents |

**Used By:** project-docs-manager, procurement-manager

### negotiation/
Contractor negotiation knowledge base (77KB of proven frameworks).

| File | Purpose |
|------|---------|
| `negotiation-foundations-guide.md` | Core negotiation principles |
| `negotiation-frameworks-comprehensive-guide.md` | Full framework reference |
| `negotiation-communication-techniques.md` | Communication tactics |
| `negotiation-playbook-integrated-approach.md` | Complete playbook |

**Used By:** procurement-manager (via `sops/sop-contractor-negotiation-prep.md`)

---

## Usage

These are reference documents - read-only knowledge base.

**Agents reference via SOPs:**
- procurement-manager reads negotiation guides during prep
- project-docs-manager references JBCC for compliance

**Templates are separate:**
- Executable negotiation templates → `templates/negotiation/`
- Reference knowledge → `references/negotiation/`

---

**See Also:**
- `templates/` - Actionable templates that use this knowledge
- `sops/` - Procedures that reference these documents
