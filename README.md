[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kWqlw--c)
# CTI-110_L5
Teaching HTML Forms, including Post and Get attributes

## Assignment: Create a Small HTML File with a Form and a Video

Objective: build a single HTML file that demonstrates a basic web form and an embedded video. The file should be valid, accessible, and easy to test in a browser.

Deliverable
- A single site named `assignment.html` placed in your L5_assignment folder. This also needs a linked style.css file. 

Requirements
- Include a semantic page structure (doctype, html, head, body, title).
- Add a form with:
    - A visible heading and short description.
    - At least these inputs: a text input (name), an email input, a select or radio group (choice), a checkbox, a textarea, and a submit button.
    - Use `label` elements correctly linked to inputs (for accessibility).
    - Set the form `method` to either `GET` or `POST` and set `action` to a test endpoint (e.g., `https://httpbin.org/post` for POST or `https://httpbin.org/get` for GET) or `#` for local testing. Include a one-line comment explaining your choice.
    - Use HTML5 validation attributes (`required`, `pattern`, `minlength`, etc.) on at least two fields.
- Embed a video:
    - Use the HTML5 `<video>` element with `controls`.
    - Download a sample video file from https://www.pexels.com/search/videos/. 
    - Reference a local file (e.g., `media/sample.mp4`), and include fallback text.
    - Optionally include a captions/subtitles `<track>` element and a short caption file (or explain how to add one).
- Accessibility & semantics:
    - Provide accessible alt/fallback text and ensure labels are clear.
    - Use semantic elements (section, header, main) where appropriate.
- CSS styling:
    - Add minimal CSS using a new style.css file (do not use the existing styles.css file) to make the form readable and responsive.
- Inline comments:
    - Add brief comments explaining key choices (method, validation, video source).

Testing
- Open `assignment.html` in a modern browser and:
    - Verify the video plays with controls.
    - Fill out the form and submit; if using an external test endpoint you should see form data echoed, otherwise verify no errors and expected behavior.

Grading rubric (example)
- Functionality (40%): form submits, validations work, video plays.
- Structure & semantics (20%): correct HTML5 structure, labels, accessibility.
- Requirements completeness (25%): all required inputs and video present.
- Presentation & comments (10%): readable layout and explanatory comments.
- Final touches (5%): captions for the video, responsive design.

Hints
- Use `required` and `type="email"` for basic validation.
- For local video testing, place the MP4 in the same folder and reference it as `media/sample.mp4`.

Submission
- Upload `assignment.html` (and any media files) to your repository.
- Include your name and date in an HTML comment at the top of the file.

Good luck — keep it simple and accessible.