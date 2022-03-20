from math import sin


class Controlador:
	"""
		Controlador PID de constantes
		Kp = 18300.84
		Ki = 3072.25
		Kd = 22688.05
		N = 31.53
	"""

	def __init__(self, ell=7, dt=0.1):
		self.ell = ell
		self.F = 0
		self.Kp = 18300.84/100
		self.Ki = 3072.25
		self.Kd = 22688.05
		self.N = 31.53
		self.tau = self.Kd / (self.N * self.Kp)
		self.e1 = 0
		self.e2 = 0
		self.d1 = 0
		self.d2 = 0
		self.fd = 0
		self.set_dt(dt)
		self.setpoint = -5

	def set_ell(self, ell):
		self.ell = ell

	def set_dt(self, dt):
		self.dt = dt
		self.A0 = self.Kp + self.Ki*self.dt
		self.A1 = -self.Kp
		self.A0d = self.Kd / self.dt
		self.A1d = -2 * self.Kd / self.dt
		self.A2d = self.Kd / self.dt
		self.alpha = self.dt / (2 * self.tau)

	def set_setpoint(self, sp):
		self.setpoint = sp

	def next(self, theta, xv):
		xc = xv + sin(theta) * self.ell
		e = self.setpoint - xc
		# PI
		self.F += self.A0 * e + self.A1 * self.e1
		# Filtered D
		self.d2 = self.d1
		self.d1 = self.A0d * e + self.A1d * self.e1 + self.A2d * self.e2
		self.fd = ((self.alpha) / (self.alpha + 1)) * (self.d1 + self.d2) - ((self.alpha - 1) / (self.alpha + 1)) * self.fd

		self.F += self.fd

		# Update errors
		self.e2 = self.e1
		self.e1 = e

		# Saturate signal
		if self.F > 2000:
			self.F = 2000
		elif self.F < -2000:
			self.F = -2000

		return self.F

