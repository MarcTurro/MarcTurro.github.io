
import * as THREE from 'three';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

function main() {

	const canvas = document.querySelector( '#c' );
	const renderer = new THREE.WebGLRenderer( { antialias: true, canvas } );
	// camera
	const fov = 75;
	const aspect = 2; // the canvas default
	const near = 0.1;
	const far = 100;
	const camera = new THREE.PerspectiveCamera( fov, aspect, near, far );
	camera.position.z = 4;
	// scene
	const scene = new THREE.Scene();
	
	// light
    const color = 0xFFFFFF;
    const intensity = 3;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(-1, 10, 10);
    scene.add(light);
    // Contrôles de la caméra
    const controls = new OrbitControls( camera, canvas );
	controls.target.set( 0, 0, 0 );
	controls.update();
	// testure 3D
    const loader = new THREE.CubeTextureLoader();
		const texture = loader.load( [
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/pos-x.jpg',
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/neg-x.jpg',
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/pos-y.jpg',
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/neg-y.jpg',
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/pos-z.jpg',
			'https://threejs.org/manual/examples/resources/images/cubemaps/computer-history-museum/neg-z.jpg',
		] );
	scene.background = texture;



    /*------------- LETTRE -------------------------*/
    // Stockage des lettres
    const lettres = {
        N: null,
        S: null,
        I: null
    };

    /**
     * Fonction pour créer une lettre 3D
     * @param {string} texte - La lettre à afficher
     * @param {number} color - Couleur hexadécimale
     * @param {number} posX - Position X
     * @param {THREE.Scene} scene - La scène Three.js
     */
    function creerLettre(texte, color, posX, scene) {
        const material = new THREE.MeshPhongMaterial({
            color: color,
            shininess: 100,
            specular: 0x444444
        });

        const loader = new FontLoader();
        loader.load(
            'https://threejs.org/examples/fonts/helvetiker_bold.typeface.json',
            function(font) {
                const geometry = new TextGeometry(texte, {
                    font: font,
                    size: 2,
                    height: 0.2,
                    depth: 0.1,
                    curveSegments: 12,
                    bevelEnabled: true,
                    bevelThickness: 0.1,
                    bevelSize: 0.05,
                    bevelSegments: 5
                });
                
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.x = posX;
                
                // Stockage de la lettre
                lettres[texte] = mesh;
                
                // Ajout à la scène
                scene.add(mesh);
            }
        );
    }

// Utilisation : créer les trois lettres
creerLettre('N', 0x44aa88, -2, scene);
creerLettre('S', 0x88aa44, 0, scene);
creerLettre('I', 0xeeaa44, 2, scene);

/*--------------FIN--------------------------------*/

// best render
function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
        renderer.setSize(width, height, false);
    }
    return needResize;
}

function render(time) {
    time *= 0.001; // convert time to seconds
    
    // Rotation de toutes les lettres
    if (lettres.N && lettres.S && lettres.I) {
        lettres.N.rotation.x = 2 * time;
        lettres.N.rotation.y = 4 * time;
        lettres.S.rotation.x = 2 * time;
        lettres.S.rotation.y = 2 * time;
        lettres.I.rotation.x = 2 * time;
        lettres.I.rotation.y = 2 * time;
    }
    
    // Résolution du problème d'étirement
    const canvas = renderer.domElement;
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
    
    // Résolution du problème de Pixelisation
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
    }
    
    // Mise à jour des contrôles
    controls.update();
    renderer.render(scene, camera);
    
    requestAnimationFrame(render);
}



requestAnimationFrame( render );
    
}


main();

 