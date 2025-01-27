locals {
  lambda_image = "${aws_ecr_repository.thoughtful_ai_lambdas.repository_url}:latest"
}

resource "aws_lambda_function" "package_sorter" {
  image_uri     = local.lambda_image
  package_type  = "Image"
  function_name = "package-sorter"
  architectures = ["arm64"]
  role          = aws_iam_role.thoughtful_ai_role
  image_config {
    command = ["src.package_sorter.handler.lambda_handler"]
  }
  timeout     = 120
  memory_size = 256
}