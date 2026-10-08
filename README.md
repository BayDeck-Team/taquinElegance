# Taquin Élégance — page de présentation

Site statique en français pour présenter le jeu de taquin sur iPhone et iPad.
HTML et CSS natifs, sans dépendance navigateur, police distante, suivi ou JavaScript applicatif.

## Aperçu local

```sh
python3 -m http.server 4173 --directory public
```

Ouvrir http://localhost:4173. Le dossier `public/` constitue le site complet à héberger.

## Publication

Le remote SSH est `git@github.com:BayDeck-Team/taquinElegance.git`.
Le workflow `.github/workflows/pages.yml` publie `public/` après un push sur `main`.
Dans GitHub, sélectionner **Settings → Pages → Source → GitHub Actions** avant le premier déploiement.

URL configurée par défaut : https://baydeck-team.github.io/taquinElegance/
En cas de domaine personnalisé, remplacer cette URL dans `public/index.html`
(canonical, Open Graph, Twitter et données structurées), `public/robots.txt` et `public/sitemap.xml`.

## Contenu à finaliser

- Ajouter le lien App Store officiel aux boutons lorsqu’il est disponible. Pour l’instant, les boutons ouvrent les sections de découverte, sans lien de téléchargement inventé.
- Confirmer le domaine définitif avant l’indexation.
- La présentation décrit uniquement les fonctions visibles sur les captures fournies ; aucun prix, avis, score ou promesse de confidentialité n’est inventé.

## Images

Les PNG à la racine sont les originaux. Seules les versions optimisées dans `public/assets/` sont publiées.
Les recadrages isolent les appareils pour la présentation. Pour les régénérer :

```sh
python3 -m pip install Pillow
python3 scripts/optimize_images.py
```

Pillow est seulement nécessaire à la régénération des images, pas au déploiement.

## SEO, accessibilité et performance

- HTML sémantique, un H1, texte indexable, langue française et FAQ native.
- Titre, description, canonical, Open Graph, Twitter Card, données structurées SoftwareApplication, robots et sitemap.
- WebP responsive, dimensions explicites, priorité à l’image du hero, chargement différé des autres visuels.
- Polices système, aucun appel tiers et aucun script exécuté.
- Navigation clavier, lien d’évitement, focus visible et respect de la préférence de mouvement réduit.

Audit local (serveur démarré dans un autre terminal) :

```sh
npx --yes lighthouse http://localhost:4173 --chrome-flags="--headless --no-sandbox" --output=json --output-path=/tmp/user/1000/opencode/taquin-lighthouse.json
```

Le score PageSpeed Insights réel dépendra aussi de l’hébergement, de la compression HTTP et du cache. Le mesurer à nouveau après publication.
