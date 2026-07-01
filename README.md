# Precompta

Application web de pré-comptabilité développée avec Django.

## Structure des apps

| App | Rôle |
|---|---|
| `core/` | Classes communes, helpers, base models, constantes |
| `accounts/` | Utilisateurs, login, custom user |
| `organizations/` | Cabinets comptables, équipes, memberships, rôles |
| `clients/` | Dossiers clients gérés par le cabinet |
| `documents/` | Upload PDF/images, stockage, hash, statuts |
| `ocr/` | Traitement OCR brut |
| `extraction/` | Extraction intelligente des champs de facture |
| `accounting/` | Plan comptable, comptes, TVA, journaux |
| `suppliers/` | Fournisseurs |
| `customers/` | Clients finaux des sociétés |
| `banking/` | Relevés bancaires, transactions |
| `reconciliation/` | Rapprochement facture ↔ paiement |
| `exports/` | Export Excel, CSV, PDF |
| `dashboard/` | Statistiques, KPIs |
| `notifications/` | Alertes, emails, notifications internes |
| `audit/` | Historique des actions |
| `billing/` | 
| `integrations/` | API externes, logiciels comptables |
| `support/` | Tickets support, assistance |

## Stack technique

- Django
- Django REST Framework
- PostgreSQL
- Docker
- Redis
- Celery
- MinIO / S3
