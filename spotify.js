import { LitElement, html } from "lit";

export class Spotify extends LitElement {
  static get properties() {
    return {
      data: Object
    }
  }

  connectedCallback() {
    super.connectedCallback();
    this.fetchData();

  }

  fetchData() {
      fetch('https://api.spotify.com/v1/me/playlists', {
        method: 'GET',
        headers: {'Authorization': '{AUTHORIZATION TOKEN}' }
      })
        .then(async response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            };
            return await response.json();
        })
        .then(data => {
          this.data = data;
          console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
  }
      
    // Render the UI as a function of component state
    render() {
      console.log(this.data)
      return html`
        ${this.data}
        <p>Spotify App!</p>
      `;
    }
}

customElements.define('spotify-app', Spotify);
