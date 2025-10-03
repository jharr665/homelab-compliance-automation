package k8s.security

deny[msg] {
  input.kind == "Deployment"
  some i
  container := input.spec.template.spec.containers[i]
  not container.securityContext.runAsNonRoot
  msg := sprintf("Container %s must set runAsNonRoot=true", [container.name])
}
