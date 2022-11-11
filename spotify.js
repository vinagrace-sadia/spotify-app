import { LitElement, html } from "lit";

export class Spotify extends LitElement {
    static properties = {
        name: {},
      };
      
      constructor() {
        super();
        // Declare reactive properties
        this.name = 'Application';
      }
    
      // Render the UI as a function of component state
      render() {
        return html`<p>Spotify ${this.name}!</p>`;
      }
}

customElements.define('spotify-app', Spotify);
