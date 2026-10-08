# Taquin Élégance — page de présentation

Site statique bilingue pour présenter le jeu de taquin sur iPhone et iPad : anglais par défaut, français sous `/fr/`.
HTML et CSS natifs, sans dépendance navigateur, police distante, suivi ou JavaScript applicatif.

## Aperçu local

```sh
python3 -m http.server 4173
```

Ouvrir http://localhost:4173 pour l’anglais ou http://localhost:4173/fr/ pour le français. Le site se compose de `index.html`, `fr/index.html`, `styles.css`, `robots.txt`, `sitemap.xml` et du dossier `assets/`, à la racine du dépôt.

## Langues

- Anglais (défaut) : https://baydeck-team.github.io/taquinElegance/
- Français : https://baydeck-team.github.io/taquinElegance/fr/
- Sélecteur EN / FR dans l’en-tête, accessible au clavier et visible sur mobile. Les liens sont relatifs au site pour fonctionner sur GitHub Pages et en local.
- Les pages sont intégralement statiques, avec traductions des contenus, textes alternatifs, libellés accessibles et métadonnées. Chaque page a son canonical et les mêmes liens réciproques `hreflang` (`en`, `fr`, `x-default`).
- Les ressources CSS et images sont communes aux deux langues ; le français les référence via `../`.

## Publication

La politique de confidentialité de l’application est disponible en anglais sous `/privacy/` et en français sous `/fr/privacy/`, avec des liens dans le pied de page. Elle indique, conformément à la déclaration de l’éditeur, qu’aucune donnée n’est collectée et que les informations restent localement dans l’application sur l’appareil.

Le remote SSH est `git@github.com:BayDeck-Team/taquinElegance.git`.
Le site fonctionne avec les deux modes de publication GitHub Pages :

- **Deploy from a branch** : sélectionner la branche `main` et le dossier `/ (root)`. Le fichier `index.html` à la racine devient la page d’accueil. `.nojekyll` désactive le traitement Jekyll.
- **GitHub Actions** : le workflow `.github/workflows/pages.yml` prépare `_site/` avec uniquement les fichiers du site puis le publie après un push sur `main`. Dans **Settings → Environments → github-pages**, autoriser la branche `main` si une restriction de branches est configurée.

Si le README apparaît sur le site, vérifier que le dernier déploiement contient bien le fichier `index.html` et qu’il a terminé avec succès.

URL configurée par défaut : https://baydeck-team.github.io/taquinElegance/
En cas de domaine personnalisé, remplacer cette URL dans `index.html` et `fr/index.html`
(canonical, Open Graph, Twitter et données structurées), `robots.txt` et `sitemap.xml`.

## Contenu à finaliser

- Ajouter le lien App Store officiel aux boutons lorsqu’il est disponible. Pour l’instant, les boutons ouvrent les sections de découverte, sans lien de téléchargement inventé.
- Confirmer le domaine définitif avant l’indexation.
- La présentation décrit uniquement les fonctions visibles sur les captures fournies ; aucun prix, avis, score ou promesse de confidentialité n’est inventé.

## Images

Les PNG à la racine sont les originaux. La page utilise uniquement les versions optimisées dans `assets/`. Le workflow GitHub Actions exclut les originaux de son artefact de publication.
Les recadrages isolent les appareils pour la présentation. Pour les régénérer :

```sh
python3 -m pip install Pillow
python3 scripts/optimize_images.py
```

Pillow est seulement nécessaire à la régénération des images, pas au déploiement.

## SEO, accessibilité et performance

- HTML sémantique, un H1 par page, texte indexable, langue explicite (`en` ou `fr`) et FAQ native.
- Titre, description, canonical, Open Graph, Twitter Card, données structurées SoftwareApplication, robots et sitemap.
- WebP responsive, dimensions explicites, priorité à l’image du hero, chargement différé des autres visuels.
- Polices système, aucun appel tiers et aucun script exécuté.
- Navigation clavier, lien d’évitement, focus visible et respect de la préférence de mouvement réduit.

Audit local (serveur démarré dans un autre terminal) :

```sh
npx --yes lighthouse http://localhost:4173 --chrome-flags="--headless --no-sandbox" --output=json --output-path=/tmp/user/1000/opencode/taquin-lighthouse.json
```

Le score PageSpeed Insights réel dépendra aussi de l’hébergement, de la compression HTTP et du cache. Le mesurer à nouveau après publication.
