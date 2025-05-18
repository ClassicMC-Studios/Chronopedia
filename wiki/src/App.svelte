<script>
  let title = "Liberty";
  let neww = '';
  let lang = 'en';
  let html;
  let year = "2025"

  function handle(e) {
    if (e.key === 'Enter') {
      title = neww;
      rizz();
    }
  }

  async function rizz() {
    try {
      let response = await fetch("http://127.0.0.1:5000/post", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          content: title,
          year: year,
          lang: lang
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      let result = await response.json();
      html = result;
      console.log(html);
    } catch (error) {
      console.error("Fetch error:", error);
    }
  }
  rizz();
</script>

<style>
  ::placeholder {
    font-style: italic;
    color: #888;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 40px;
    background-color: #f8f9fa;
    border-bottom: 1px solid #a2a9b1;
    position: relative;
  z-index: 1;
  }
  .header::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  right: 0;
  height: 6.7px;
  background: linear-gradient(to bottom, rgba(0,0,0,0.05), rgba(0,0,0,0));
  pointer-events: none;
}

  .logo {
    height: 50px;
    background-color: #f8f9fa;
    margin-bottom:5px;
  }

  .inputs {
    display: flex;
    gap: 8px;
  }

  .main {
    padding: 2rem 1rem;
  }
  a {
  font-size: 20px;
  background-color: #f8f9fa;
    }
</style>

<div class="header">
  <img src="https://guyotjs.github.io/mee.png" class="logo" alt="CopypediA" />

  <div class="inputs">
    <input
      type="text"
      placeholder="Search Chronopedia"
      bind:value={neww}
      on:keydown={handle}
    />
    <a target="_blank" href="http://127.0.0.1:5000/audio">Text to Speech</a>
    <input
      type="text"
      placeholder="en"
      bind:value={lang}
      on:keydown={handle}
      style="width: 40px;"
    />
    <input
      type="text"
      placeholder="year"
      bind:value={year}
      on:keydown={handle}
      style="width: 50px;"
    />
  </div>
</div>

<div class="main">
  {#key title}
    <h1>{title.replaceAll("_", " ")}</h1>
    {@html html}
  {/key}
</div>
