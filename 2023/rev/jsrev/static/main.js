import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import KeyboardState from './KeyboardState.js';

function start(){
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    const keyboard = new KeyboardState();
    const controls = new OrbitControls( camera, renderer.domElement );

    const boxA = new THREE.BoxGeometry( 1, 1, 1 );
    const matA = new THREE.MeshBasicMaterial( { color: 0x00ff00, wireframe: true } );
    const cubeA = new THREE.Mesh( boxA, matA );
    scene.add( cubeA );

    const boxB = new THREE.BoxGeometry( 1, 1, 1 );
    const matB = new THREE.MeshBasicMaterial( { color: 0x0000ff } );
    const cubeB = new THREE.Mesh( boxB, matB );
    cubeB.position.x = 2;
    scene.add( cubeB );

    camera.position.z = 10;

    let rays = [];
    function animate() {
        requestAnimationFrame( animate );
        renderer.render( scene, camera );
        update();
    }
    animate();

    function update(){
        console.log(rays);
        for (var ray of rays){
            scene.remove(ray);
        }
        rays = [];
        keyboard.update();
        if (keyboard.pressed("left")){
            cubeA.position.x -= 0.1;
        }
        if (keyboard.pressed("right")){
            cubeA.position.x += 0.1;
        }
        if (keyboard.pressed("up")){
            cubeA.position.y += 0.1;
        }
        if (keyboard.pressed("down")){
            cubeA.position.y -= 0.1;
        }

        if (keyboard.pressed("A")){
            console.log("A");
            cubeB.position.x -= 0.1;
        }
        if (keyboard.pressed("D")){
            cubeB.position.x += 0.1;
        }
        if (keyboard.pressed("W")){
            cubeB.position.y += 0.1;
        }
        if (keyboard.pressed("S")){
            cubeB.position.y -= 0.1;
        }
        controls.update();

        const boxB = new THREE.Box3().setFromObject( cubeB );

        var vertices = [];
        const vector = new THREE.Vector3();
        for ( let i = 0, l = cubeA.geometry.attributes.position.count; i < l; i ++){
            vector.fromBufferAttribute( cubeA.geometry.attributes.position, i );
            vector.applyMatrix4( cubeA.matrixWorld );
            vertices.push( vector );
        }

        var collided = false;
        for (var vertexIndex = 0; vertexIndex < vertices.length; vertexIndex++)
        {       
            var localVertex = vertices[vertexIndex].clone();
            var directionVector = localVertex.sub(cubeA.position);
        

            var ray = new THREE.Ray( cubeA.position, directionVector);
            var rayViz = new THREE.ArrowHelper(ray.direction, ray.origin, 1, 0xff0000)
            scene.add(rayViz);
            rays.push(rayViz);
 
            if ( ray.intersectsBox( boxB ) ) 
            {
                console.log("XX");
                collided = true;
            }
            
        }
        if (collided){
            cubeA.material.color.setHex( 0xff0000 );    
        }
        else {
            cubeA.material.color.setHex( 0x00ff00 );
        }
    }
}
window.start = start;