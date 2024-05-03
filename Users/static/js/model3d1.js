import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

renderer.outputColorSpace = THREE.SRGBColorSpace;

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000, 0);
renderer.setPixelRatio(window.devicePixelRatio);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
camera.position.set(4, 5, 11);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.enablePan = false;
controls.minDistance = 5;
controls.maxDistance = 20;
controls.minPolarAngle = 0.5;
controls.maxPolarAngle = 1.5;
controls.autoRotate = false;
controls.target = new THREE.Vector3(0, 1, 0);
controls.update();

const groundGeometry = new THREE.PlaneGeometry(20, 20, 32, 32);
groundGeometry.rotateX(-Math.PI / 2);
const groundMaterial = new THREE.MeshStandardMaterial({
  color: 0x555555,
  side: THREE.DoubleSide
});
const groundMesh = new THREE.Mesh(groundGeometry, groundMaterial);

groundMaterial.transparent = true;
groundMaterial.opacity = 0.8;
groundMesh.castShadow = false;
groundMesh.receiveShadow = true;
groundMaterial.color.set(0xeeeeee);
scene.add(groundMesh);

const spotLightFront = new THREE.SpotLight(0xffffff, 3000, 100, 0.22, 1);
spotLightFront.position.set(0, 25, 12); // Position in front of the model
spotLightFront.castShadow = true;
spotLightFront.shadow.bias = -0.0001;
scene.add(spotLightFront);

const spotLightRear = new THREE.SpotLight(0xffffff, 3000, 100, 0.22, 1);
spotLightRear.position.set(0, 25, -12); // Position behind the model
scene.add(spotLightRear);

const loader = new GLTFLoader().setPath('3d/2284_legroscollardfloriane_femalemuscle/');
loader.load('scene.gltf', (gltf) => {
  console.log('loading model');
  const mesh = gltf.scene;

  mesh.traverse((child) => {
    if (child.isMesh) {
        //child.material.color.set(0xff0000);
        child.castShadow = true;
        child.receiveShadow = true;
    }
  });

  mesh.position.set(0, -4, -1);
  mesh.scale.set(5, 5, 5);
  scene.add(mesh);

  document.getElementById('model2').appendChild(renderer.domElement);
}, (xhr) => {
  console.log(`loading ${xhr.loaded / xhr.total * 100}%`);
}, (error) => {
  console.error(error);
});

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});


groundMesh.position.y = -5; // Move the floor down to a y-coordinate of -1


function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

animate();


// Adjust camera aspect ratio when the div size changes
function onWindowResize() {
  const width = document.getElementById('model2').clientWidth;
  const height = document.getElementById('model2').clientHeight;
  
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

// Call onWindowResize initially and on window resize event
onWindowResize();
window.addEventListener('resize', onWindowResize);

