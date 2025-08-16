(() => {
  const canvas = document.getElementById('bg');
  const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Renderer
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: true, powerPreference: 'high-performance' });
  const DPR = Math.min(window.devicePixelRatio || 1, prefersReduced ? 1 : 1.5);
  renderer.setPixelRatio(DPR);

  // Scene & Camera
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, 1, 0.1, 100);
  camera.position.set(0, 0, 5);

  // Lights
  const al = new THREE.AmbientLight(0xffffff, 0.6);
  scene.add(al);
  const dl = new THREE.DirectionalLight(0xffffff, 1.0);
  dl.position.set(5, 5, 5);
  scene.add(dl);

  // Starfield
  const starCount = window.innerWidth < 768 ? 800 : 1800;
  const starGeom = new THREE.BufferGeometry();
  const starPos = new Float32Array(starCount * 3);
  for (let i = 0; i < starCount; i++) {
    starPos[i * 3 + 0] = (Math.random() - 0.5) * 30;
    starPos[i * 3 + 1] = (Math.random() - 0.5) * 30;
    starPos[i * 3 + 2] = (Math.random() - 0.5) * 30;
  }
  starGeom.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
  const stars = new THREE.Points(
    starGeom,
    new THREE.PointsMaterial({ size: 0.03, transparent: true, opacity: 0.75 })
  );
  scene.add(stars);

  // Torus Knot
  const knotGeom = new THREE.TorusKnotGeometry(1.1, 0.34, 220, 16);
  const knotMat = new THREE.MeshStandardMaterial({ metalness: 0.7, roughness: 0.25, color: 0x60a5fa });
  const knot = new THREE.Mesh(knotGeom, knotMat);
  scene.add(knot);

  // Resize handler
  function resize() {
    const w = window.innerWidth, h = window.innerHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  // Scroll → progress (0..1)
  let progress = 0;
  function onScroll() {
    const max = document.body.scrollHeight - window.innerHeight;
    progress = max > 0 ? window.scrollY / max : 0;
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Animation
  let last = performance.now();
  function tick(now) {
    const dt = Math.min((now - last) / 1000, 0.1); // clamp delta
    last = now;

    if (!prefersReduced) {
      stars.rotation.y += dt * 0.06;
      knot.rotation.x += dt * 0.25;
      knot.rotation.y += dt * 0.18;
    }

    // Scroll-reactive path
    knot.position.y = 2 - progress * 8; // moves up as you scroll
    knot.position.x = Math.sin(progress * Math.PI * 2) * 1.2;

    renderer.render(scene, camera);
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
