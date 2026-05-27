<div align="center">
  <h1>Browsy</h1>
  
  <p>Modular Web Browser Architecture Project</p>
</div>

<hr>

<h2>Architecture Overview</h2>
<div align="center">
  <img src="assets/architecture/browsy_architecture.png" width="800">
</div>

<hr>

<h2>🔄 Browser Flow</h2>
<p align="center">
  User Input → UI → Core → Network → Renderer → Screen
</p>

<div align="center">
  <img src="assets/architecture/flow_diagram.png" width="750">
</div>

<hr>

<h2>🧩 Modules</h2>
<div align="center">
  <img src="assets/architecture/modules.png" width="800">
</div>

<hr>

<h2></h2> UI Concept</h2>
<div align="center">
  <img src="assets/architecture/ui_mockup.png" width="800">
</div>

<hr>

<h2>⚙️ Rendering Pipeline</h2>
<p align="center">
  HTML → DOM → CSS → Layout → Paint
</p>

<div align="center">
  <img src="assets/architecture/renderer_pipeline.png" width="800">
</div>

<hr>

<h2>Goal</h2>
<p align="center">
  Browsy is a minimal browser engine built to understand how web browsers actually work internally.
</p>

<hr>

<h2>📁 Structure</h2>
<pre>
Browsy/
├── core/
├── network/
├── renderer/
├── js_engine/
├── storage/
├── ui/
├── platform/
├── tests/
├── assets/
├── docs/
└── main.py
</pre>
