# Active Projects

This directory contains active project documentation and tracking.

**Last Updated:** 2025-11-08

---

## 📁 Directory Contents

### Project Template

**[_TEMPLATE_PMP_PROJECT/](_TEMPLATE_PMP_PROJECT/)**
- Complete PMP-aligned project folder structure
- Phase-based organization (Initiation → Planning → Design → Execution → Handover)
- Ready-to-use template for new projects
- See [_TEMPLATE_PMP_PROJECT/README.md](_TEMPLATE_PMP_PROJECT/README.md) for details

---

### Active Projects

**[11_Buck_Road](11_Buck_Road)** (Symlinked)
- **Type:** Symlink to Google Drive
- **Location:** `~/Library/CloudStorage/GoogleDrive-dlproudfoot@gmail.com/My Drive/B.Client Execution/2.11_Buck_Road`
- **Status:** Active client project
- **Integration:** Files managed in Google Drive, accessible via AGENT system

**Slash Command:** `/organize_inbox 11buck` - Organize project inbox files

---

## 🎯 Project Management Approach

### Two-Tier Architecture

**Tier 1: Project Files (Knowledge & Context)**
- Complete project documentation
- Persistent institutional knowledge
- PMP-aligned folder structure
- Reference materials and decisions

**Tier 2: AI Agents (Operations)**
- Status reports and client communication
- Procurement and LOI generation
- Budget analysis and tracking
- Document organization

### Integration
- **Project files** provide WHY and HOW with full context
- **Claude AI agents** handle operational tasks intelligently

---

## 📂 Standard Project Structure

All projects follow PMP-aligned folder structure (see `_TEMPLATE_PMP_PROJECT/`):

```
[Project_Name]/
├── 00-inbox/               # Unsorted incoming files
├── 01-initiation/          # Feasibility, requirements, property details
├── 02-planning/            # Fee proposals, program, PM plan
├── 03-design/              # Design submissions and viability
├── 04-consultants/         # Civil, electrical, structural, etc.
│   ├── Architect/
│   ├── Civil_Engineer/
│   ├── Electrical_Engineer/
│   ├── Quantity_Surveyor/
│   └── Structural_Engineer/
├── 05-procurement/         # Orders, quotations, LOIs
├── 06-compliance/          # Approvals, safety, regulations
├── 07-execution/           # Construction phase documents
├── 08-handover/            # Completion, snag lists, as-builts
├── 09-meetings/            # Meeting minutes and agendas
└── logs/                   # Organization logs, automation records
```

---

## 🚀 Starting a New Project

### Option 1: Copy Template
```bash
cp -r ~/AGENT/projects/_TEMPLATE_PMP_PROJECT ~/AGENT/projects/[NEW_PROJECT_NAME]
```

### Option 2: Google Drive Integration
```bash
# Create symlink to Google Drive project
ln -s ~/Library/CloudStorage/GoogleDrive-*/path/to/project ~/AGENT/projects/[PROJECT_NAME]
```

### Option 3: Use Slash Command
Ask Claude: `/organize_inbox [project_name]` to set up automated inbox processing

---

## 📋 Project File Management

### File Naming Standard

**Format:** `[Company_Name]_[Document_Type]_[Date_YYYYMMDD].[extension]`

**Examples:**
- `Franki_Africa_Quote_20251008.pdf`
- `Geomech_Africa_Report_20250305.pdf`
- `ABC_Structural_Drawing_Set_A_20250115.pdf`

**See:** [File Organization SOP](../sops/sop-project-file-organization.md)

---

## 🔗 Related Documentation

### SOPs
- [Project File Organization SOP](../sops/sop-project-file-organization.md) - File structure and naming
- [LOI Management SOP](../sops/sop-loi-management.md) - Procurement process

### System Documentation
- [System Architecture](../docs/SYSTEM-ARCHITECTURE.md) - Two-tier design
- [PMP Framework Automation](../memories/pmp-framework-automation.md) - PMP alignment

### Slash Commands
- `/organize_inbox [project]` - Automated inbox organization
- `/capture_workflow` - Document new project workflows

---

## 🎓 For Project Managers

### Daily Workflow
1. **Morning:** Review project priorities and pending items
2. **Throughout Day:** Drop incoming files into `00-inbox/`
3. **End of Day:** Ask Claude to organize inbox: `/organize_inbox [project]`
4. **Weekly:** Review project file structure for completeness

### Using the Template
1. Start every project with `_TEMPLATE_PMP_PROJECT/` structure
2. Customize consultant folders based on actual consultants
3. Maintain phase-based organization throughout project lifecycle
4. Use `/organize_inbox` for automated file categorization

### Best Practices
- **Inbox Zero:** Process inbox regularly, don't let files accumulate
- **Consistent Naming:** Follow file naming standards for searchability
- **Phase Organization:** Keep documents in correct phase folders
- **Document Decisions:** Capture key decisions in meeting minutes
- **Lessons Learned:** Document insights in `08-handover/lessons-learned/`

---

## 📊 Current Portfolio Status

**Active Projects:** 1
- 11_Buck_Road (Client execution phase)

**Project Template:** Available
- _TEMPLATE_PMP_PROJECT (Ready for new projects)

**Planned Capacity:** 3-5 concurrent projects

---

## 🔍 Quick Commands

**List all projects:**
```bash
ls -l ~/AGENT/projects/ | grep -v "_TEMPLATE"
```

**Find files in a project:**
```bash
find ~/AGENT/projects/[PROJECT_NAME] -name "*.pdf"
grep -r "search term" ~/AGENT/projects/[PROJECT_NAME]
```

**Organize project inbox:**
Ask Claude: `/organize_inbox [project_name]`

**Create new project:**
```bash
cp -r ~/AGENT/projects/_TEMPLATE_PMP_PROJECT ~/AGENT/projects/[NEW_PROJECT]
```

---

**Owner:** Donovan Proudfoot
**Company:** Proman Project Management
**Last Updated:** 2025-11-08
