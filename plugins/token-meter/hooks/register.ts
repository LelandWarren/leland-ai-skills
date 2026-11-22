import type { Register, SessionContextUsage } from 'claude-code'

// 93350 -> "93k", 1000000 -> "1M"
export const short = (n: number): string => {
  if (n >= 1_000_000) return `${+(n / 1_000_000).toFixed(1)}M`
  if (n >= 1_000) return `${Math.round(n / 1_000)}k`
  return `${n}`
}

// undefined until the first response reports a fill, which leaves the line empty.
export const label = (c: SessionContextUsage): string | undefined => {
  if (c.tokens === undefined) return undefined
  const percent = c.percent ?? Math.round((c.tokens / c.window) * 100)
  return `${short(c.tokens)} / ${short(c.window)} tokens (${percent}%)`
}

// The status line under the prompt is the one spot the desktop app reliably
// shows for every mod; the band above the prompt can be held by another mod.
export const register: Register = on => {
  // Fill it in right away, so a resumed chat shows its count before the next turn.
  on('session.start', async ($, e, next) => {
    const { context } = await $.session.usage()
    $.ui.status(label(context))
    return next(e)
  })

  // The engine pushes new figures after each turn.
  on('session.measure', ($, e, next) => {
    if (e.changed.includes('context')) $.ui.status(label(e.context))
    return next(e)
  })
}
