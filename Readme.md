# Django Project with OpenAI and Keras OCR

Welcome to the repository for the Django project incorporating OpenAI API for product description generation and Keras OCR for image keyword extraction.

## Project Overview

This Django project includes several API endpoints for user registration, login, product description generation, and image keyword extraction.

### Endpoints

#### User Registration
- **Endpoint:** `/register/`
- **Description:** Register a new user.
- **Usage:** `POST` request to register a user.
- **Request:** `username`,`email`, `password`
- **Response:** `token`

#### User Login
- **Endpoint:** `/login/`
- **Description:** Login with registered credentials.
- **Usage:** `POST` request to authenticate and log in.
- **Request:** `username`,`password`
- **Response:** `token`

#### Generate Product Description
- **Endpoint:** `/generate-product-description/`
- **Description:** Generate detailed product descriptions using the OpenAI API.
- **Usage:** `POST` request with the product title to receive a generated product description.
- **Request:** `product_title`
- **Response:** `description`, `keywords`


#### Image Keyword Extraction
- **Endpoint:** `/image-keyword/`
- **Description:** Extract keywords from uploaded images using Keras OCR.
- **Usage:** `POST` request to upload an image and receive extracted keywords.
- **Request:** `image`
- **Response:** `keywords`

## Technologies Used

- Django: Web framework for building APIs.
- OpenAI API: Utilized for generating detailed product descriptions.
- Keras OCR: Used for image keyword extraction from uploaded images.
- Tensorflow: Used for running keras image processing models.

## Getting Started

1. Clone the repository.
   ```bash
   git clone https://github.com/your-username/Backend-Project-for-Text-Completion-and-Image-Recognition.git

2. 
