import './App.css';

function App() {
  return (
    /*  <div className="App">
        <header className="App-header">
          <img src="Octocat.png" className="App-logo" alt="logo" />
          <p>
            GitHub Codespaces <span className="heart">♥️</span> React
          </p>
          <p className="small">
            Edit <code>src/App.jsx</code> and save to reload.
          </p>
          <p>
            <a
              className="App-link"
              href="https://reactjs.org"
              target="_blank"
              rel="noopener noreferrer"
            >
              Learn React
            </a>
          </p>
        </header>
      </div>*/
  <div className="main">
      <div className="column">
          <div className="titleItem"><h2>Send</h2></div>
          <div class="subheading"><h3>Upload files to send</h3></div>
          <div><input type="file" id="my_file_input" /></div>
      </div>
      <div className="column">
          <div className="titleItem"><h2>Recieve</h2></div>
          <div className="subheading"><h3>New Files will Appear Here</h3></div>
          <div className="imagePreview">
            <div>hello.png</div>
            <img src="flower.jpeg"></img>
          </div>
      </div>
  </div>

  );
}

export default App;