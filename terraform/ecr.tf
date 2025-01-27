resource "aws_ecr_repository" "thoughtful_ai_lambdas" {
  name                 = "thoughtful-ai-lambdas"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}