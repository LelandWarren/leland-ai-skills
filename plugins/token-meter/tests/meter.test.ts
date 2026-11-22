import { expect, test } from 'claude-code/testing'

import { label, short } from '../hooks/register'

test('short() rounds to k and M', async () => {
  expect(short(512)).toBe('512')
  expect(short(93_350)).toBe('93k')
  expect(short(1_000_000)).toBe('1M')
  expect(short(1_250_000)).toBe('1.3M')
})

test('label() is empty before the first reading', async () => {
  expect(label({ window: 1_000_000 })).toBeUndefined()
})

test('a turn sets the status line to the count', async ($, on) => {
  const lines: (string | undefined)[] = []
  on('ui.status', (_$, e) => { lines.push(e.text); return { value: undefined } })
  on('session.measure', (_$, e) => ({ changed: e.changed }))

  await $.session.measure({
    context: { tokens: 93_350, window: 1_000_000, percent: 9 },
    rateLimits: [],
    changed: ['context'],
  })

  expect(lines).toEqual(['93k / 1M tokens (9%)'])
})

test('a turn that only moved the rate limits leaves the line alone', async ($, on) => {
  const lines: (string | undefined)[] = []
  on('ui.status', (_$, e) => { lines.push(e.text); return { value: undefined } })
  on('session.measure', (_$, e) => ({ changed: e.changed }))

  await $.session.measure({
    context: { tokens: 93_350, window: 1_000_000, percent: 9 },
    rateLimits: [],
    changed: ['rateLimits'],
  })

  expect(lines).toEqual([])
})
