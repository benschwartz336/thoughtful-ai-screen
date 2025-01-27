data "aws_iam_policy_document" "thoughtful_ai_assume_role_policy" {
  statement {
    actions = [
      "sts:AssumeRole",
      "sts:TagSession"
    ]
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::999999999999:role/thoughtful-ai-role"]
    }
  }
}

resource "aws_iam_role" "thoughtful_ai_role" {
  name               = "thoughtful-ai-role"
  assume_role_policy = data.aws_iam_policy_document.thoughtful_ai_assume_role_policy.json
}

data "aws_iam_policy_document" "thoughtful_ai_policy" {
  statement {
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "logs:DescribeLogGroups",
      "logs:GetLogEvents",
      "logs:DescribeLogStreams"
    ]
    effect    = "Allow"
    resources = ["*"]
  }
  statement {
    actions = [
      "cloudwatch:PutMetricData",
      "cloudwatch:GetMetricStatistics"
    ]
    effect    = "Allow"
    resources = ["*"]
  }
  statement {
    actions = [
      "xray:PutTraceSegments"
    ]
    effect    = "Allow"
    resources = ["*"]
  }
  statement {
    actions = [
      "ec2:CreateNetworkInterface",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DeleteNetworkInterface"
    ]
    effect    = "Allow"
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "thoughtful_ai_policy" {
  name   = "thoughtful-ai-policy"
  role   = aws_iam_role.thoughtful_ai_role.name
  policy = data.aws_iam_policy_document.thoughtful_ai_policy.json
}
