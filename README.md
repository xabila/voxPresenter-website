# VoxPresenter — Site Web

Le site marketing de VoxPresenter.

## Repos

| Repo | Visibilité | Contenu |
|------|-----------|---------|
| [xabila/voxPresenter](https://github.com/xabila/voxPresenter) | 🔒 Privé | Code source complet de l'app iOS + Mac |
| [xabila/voxPresenter-website](https://github.com/xabila/voxPresenter-website) | 🌐 Public | Site web marketing (ce dossier) |

## Déploiement

Le site est hébergé sur **GitHub Pages** via `voxPresenter-website` → [voxpresenter.com](https://voxpresenter.com)

Pour mettre à jour le site, éditer les fichiers dans `site-web/` puis synchroniser vers `voxPresenter-website` :

```bash
cp -r site-web/* /tmp/vox-website/
cd /tmp/vox-website
git add -A && git commit -m "site: ..." && git push
```

## Structure

```
index.html      # Page principale (multilingue FR/EN)
css/style.css   # Styles
js/app.js       # Traductions + détection langue
favicon.ico     # Favicon multi-tailles (16/32/48)
.nojekyll       # Désactive Jekyll si Pages republie depuis la branche
assets/
  icon.png             # Icône app (1024×1024, logos dans la page)
  favicon-32.png       # Favicon PNG 32×32
  apple-touch-icon.png # Apple touch icon 180×180
```
